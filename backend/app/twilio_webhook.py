from fastapi import Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import schemas
from .crud import create_review

# Simple in-memory conversation store. For production, replace with Redis/DB.
_conversations = {}

async def handle_twilio(request: Request):
    form = await request.form()
    from_number = form.get('From')  # e.g., 'whatsapp:+1415...'
    body = (form.get('Body') or '').strip()

    resp = MessagingResponse()

    if not from_number:
        resp.message("Invalid request: missing From")
        return PlainTextResponse(str(resp), status_code=400)

    if from_number not in _conversations:
        _conversations[from_number] = {"step": "ask_product", "product_name": None, "user_name": None, "product_review": None}
        resp.message("Which product is this review for?")
        return PlainTextResponse(str(resp), status_code=200)

    conv = _conversations[from_number]
    step = conv['step']

    if step == 'ask_product':
        conv['product_name'] = body
        conv['step'] = 'ask_name'
        resp.message("What's your name?")
        return PlainTextResponse(str(resp), status_code=200)

    if step == 'ask_name':
        conv['user_name'] = body
        conv['step'] = 'ask_review'
        resp.message(f"Please send your review for {conv['product_name']}.")
        return PlainTextResponse(str(resp), status_code=200)

    if step == 'ask_review':
        conv['product_review'] = body
        db: Session = SessionLocal()
        try:
            review = create_review(db, schemas.ReviewCreate(
                contact_number=from_number,
                user_name=conv['user_name'],
                product_name=conv['product_name'],
                product_review=conv['product_review']
            ))
        finally:
            db.close()

        resp.message(f"Thanks {conv['user_name']} -- your review for {conv['product_name']} has been recorded.")
        del _conversations[from_number]
        return PlainTextResponse(str(resp), status_code=200)

    resp.message("Sorry, I didn't understand. Please say 'Hi' to start.")
    return PlainTextResponse(str(resp), status_code=200)

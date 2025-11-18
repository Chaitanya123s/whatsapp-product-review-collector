from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base, SessionLocal
from . import models
from .crud import get_reviews
from .schemas import ReviewOut
from .twilio_webhook import handle_twilio

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/webhook/twilio')
async def twilio_webhook(request: Request):
    return await handle_twilio(request)

@app.get('/api/reviews', response_model=list[ReviewOut])
def api_get_reviews():
    db = SessionLocal()
    try:
        rows = get_reviews(db)
        return rows
    finally:
        db.close()

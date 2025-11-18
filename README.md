# WhatsApp Product Review Collector

Full-stack project (FastAPI + React + Postgres) to collect product reviews via WhatsApp (Twilio Sandbox) and display them in a React frontend.

## Quick start (Docker Compose)

1. Copy `.env.example` to `.env` and fill in your Twilio values.

2. Start the stack:

```bash
docker compose up --build
```

3. For local Twilio webhook testing use `ngrok`:

```bash
ngrok http 8000
```

Set Twilio WhatsApp Sandbox inbound webhook to `https://<your-ngrok-id>.ngrok.io/webhook/twilio` and join the sandbox from your phone.

4. Open frontend: http://localhost:3000

## Run backend locally (no Docker)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Run frontend locally

```bash
cd frontend
npm install
npm start
```

## Project structure

- `backend/` - FastAPI backend and Twilio webhook handler
- `frontend/` - React app that fetches `/api/reviews` and displays them
- `docker-compose.yml` - runs postgres, backend, and frontend

## Notes
- Conversation state is kept in memory in `backend/app/twilio_webhook.py`. For production use Redis or DB to persist state.
- The webhook expects Twilio to send `application/x-www-form-urlencoded` payloads (Twilio default).

## Delivery
- Ensure `.env` has correct Twilio sandbox credentials and `DATABASE_URL` if you change DB settings.

Good luck — if you want, I can:
- push this repo to your GitHub (I will provide git commands),
- add Redis service + update webhook to persist conversation state,
- add unit tests and CI config,
- or create a short screencast script you can record.

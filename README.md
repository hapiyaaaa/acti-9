# acti-9 — Laboratory Activity 9: System-to-System API Integration

Flask app (continues act-4) that retrieves a partner's records, saves selected ones locally, and sends a practice record to the partner.

## Run locally
    pip install -r requirements.txt
    python init_db.py
    set PARTNER_API_URL=https://PARTNER-APP.onrender.com/api/students
    python app.py

## Render
- Build: `pip install -r requirements.txt`  Start: `gunicorn app:app`
- Environment variable `PARTNER_API_URL` = partner's `/api/students` URL.

## Endpoints added
- `GET /partner-records` — server-side fetch of partner records (502 on failure)
- `POST /import-student` — save a partner record, source `Classmate API`
- `POST /send-record` — send a practice record to the partner (source `Partner API`)
- `POST /api/students` — now stores `source` (default `External API`)

Use fictional data only.

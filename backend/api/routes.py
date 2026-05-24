import os
import json
import datetime
from fastapi import APIRouter, Request, HTTPException
from backend.api.models import EnquiryRequest, ConsentLogRequest
from backend.services.email_service import send_confirmation_email

router = APIRouter()

CONSENT_LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "consent_logs.json")

@router.post("/submit-enquiry")
async def submit_enquiry(request: EnquiryRequest):
    # The Pydantic model automatically validates and sanitizes input types/lengths
    # We trigger the email service
    success = send_confirmation_email(
        name=request.name,
        email=request.email,
        course=request.course
    )
    return {"success": True, "message": "Enquiry processed successfully"}

@router.post("/log-consent")
async def log_consent(data: ConsentLogRequest, request: Request):
    ip = request.client.host if request.client else "unknown"
    user_agent = request.headers.get("User-Agent", "unknown")
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"

    log_entry = {
        "timestamp": timestamp,
        "ip_address": ip,
        "consent": data.consent,
        "user_agent": user_agent
    }

    logs = []
    if os.path.exists(CONSENT_LOG_FILE):
        try:
            with open(CONSENT_LOG_FILE, 'r') as f:
                logs = json.load(f)
        except Exception:
            pass
    
    logs.append(log_entry)
    
    with open(CONSENT_LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)

    return {"success": True}

@router.get("/get-consent-logs")
async def get_consent_logs():
    if os.path.exists(CONSENT_LOG_FILE):
        with open(CONSENT_LOG_FILE, 'r') as f:
            try:
                return json.load(f)
            except:
                return []
    return []

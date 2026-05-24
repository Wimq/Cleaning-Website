from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class EnquiryRequest(BaseModel):
    recaptcha_token: Optional[str] = None
    form_type: str = Field(..., max_length=50)
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    course: Optional[str] = Field(None, max_length=150)
    phone: Optional[str] = Field(None, max_length=20)
    details: Optional[str] = Field(None, max_length=1000)

class ConsentLogRequest(BaseModel):
    consent: str = Field(..., max_length=100)

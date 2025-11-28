from pydantic import BaseModel, field_validator

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class EmailData(BaseModel):

    message_id: str
    thread_id: Optional[str] = None

    from_email: EmailStr
    to_email: Optional[EmailStr] = None

    subject: Optional[str] = None
    raw_body: Optional[str] = None
    cleaned_body: str

    status: str = Field(default="new")
    category: Optional[str] = None
    reason: Optional[str] = None

    deadline_time: Optional[datetime] = None
    formality: Optional[str] = None
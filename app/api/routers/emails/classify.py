import logging

from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.database.client import get_db_session
from app.database.models import Emails

from app.utils.celery_client import create_classify_email_task

from app.api.models.email_data import EmailData


router = APIRouter(tags=["Authorization"])

logger = logging.getLogger(__name__)


@router.post("/classify")
async def classify_func(data: EmailData, session: AsyncSession = Depends(get_db_session)):

    email = Emails(
        message_id=data.message_id,
        thread_id=data.thread_id,
        from_email=data.from_email,
        to_email=data.to_email,
        subject=data.subject,
        raw_body=data.raw_body,
        cleaned_body=data.cleaned_body
    )

    session.add(email)

    await session.commit()
    await session.flush()

    await create_classify_email_task(application_data={"email_id": email.id})

    return JSONResponse(status_code=200, content={'message': 'Success'})
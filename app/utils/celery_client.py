from celery import Celery
from app.utils.config import REDIS_URL

celery_app = Celery(
    "llm_workers",
    broker=REDIS_URL
)

celery_app.conf.update(
    task_acks_late=True,
    broker_transport_options={"visibility_timeout": 3600},
)


def create_task(task_name: str, *args, **kwargs):
    return celery_app.send_task(task_name, args=args, kwargs=kwargs)


def create_classify_email_task(application_data: dict, **kwargs):
    return celery_app.send_task(
        'classify_email',
        args=[application_data],
        kwargs=kwargs
    )


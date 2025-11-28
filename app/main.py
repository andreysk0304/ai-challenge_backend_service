import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.database.client import create_db
from app.utils.tags import openapi_tags

from app.api.routers.emails import classify

app = FastAPI(openapi_tags=openapi_tags)


app.include_router(classify.router, prefix="/emails")

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",") if os.getenv("ALLOWED_ORIGINS") else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    await create_db()
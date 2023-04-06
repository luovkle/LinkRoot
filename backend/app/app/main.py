from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.client import client

app = FastAPI(
    license_info={
        "name": settings.APP_LICENSE_NAME,
        "url": settings.APP_LICENSE_URL,
    }
)
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.MIDDLEWARE_ALLOW_CREDENTIALS,
    allow_methods=settings.MIDDLEWARE_ALLOW_METHODS,
    allow_headers=settings.MIDDLEWARE_ALLOW_HEADERS,
)


@app.on_event("shutdown")
def shutdown_event():
    client.close()

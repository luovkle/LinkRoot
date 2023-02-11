from fastapi import APIRouter

from app.api.api_v1.endpoints.main import router as main_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(main_router)

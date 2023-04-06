from fastapi import APIRouter

from app.api.api_v1.endpoints.profiles import router as profiles_router
from app.api.api_v1.endpoints.links import router as links_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(profiles_router, prefix="/profiles", tags=["profiles"])
api_router.include_router(links_router, prefix="/links", tags=["links"])

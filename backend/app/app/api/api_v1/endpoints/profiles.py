from fastapi import APIRouter, Depends, UploadFile
from pymongo.database import Database

from app.api.deps import get_user, get_db
from app.schemas.profile import ProfileRead, ProfileUpdate

router = APIRouter()


@router.get("/@me", response_model=ProfileRead)
def get_current_profile(user: str = Depends(get_user), db: Database = Depends(get_db)):
    ...


@router.put("/@me", response_model=ProfileRead)
def update_current_profile(
    user: str = Depends(get_user),
    db: Database = Depends(get_db),
    *,
    profile: ProfileUpdate
):
    ...


@router.put("/@me/picture", response_model=ProfileRead)
def upload_current_picture(
    user: str = Depends(get_user),
    db: Database = Depends(get_db),
    *,
    picture: UploadFile
):
    ...

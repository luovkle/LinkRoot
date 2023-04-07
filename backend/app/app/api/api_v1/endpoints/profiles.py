from fastapi import APIRouter, Depends, UploadFile
from pymongo.database import Database

from app.api.deps import get_user, get_db, get_access_token
from app.schemas.profile import ProfileRead, ProfileUpdate
from app.crud.profile import crud_profile

router = APIRouter()


@router.get("/@me", response_model=ProfileRead)
def get_current_profile(
    user: str = Depends(get_user),
    access_token: str = Depends(get_access_token),
    db: Database = Depends(get_db),
):
    return crud_profile.read(db, user, access_token)


@router.put("/@me", response_model=ProfileRead)
def update_current_profile(
    user: str = Depends(get_user),
    access_token: str = Depends(get_access_token),
    db: Database = Depends(get_db),
    *,
    profile: ProfileUpdate
):
    return crud_profile.update(db, user, profile, access_token)


@router.put("/@me/picture", response_model=ProfileRead)
def upload_current_picture(
    user: str = Depends(get_user),
    access_token: str = Depends(get_access_token),
    db: Database = Depends(get_db),
    *,
    picture: UploadFile
):
    return crud_profile.update_picture(db, user, picture, access_token)

from fastapi import APIRouter, Depends, UploadFile

from app.api.deps import get_user
from app.schemas.profile import ProfileRead, ProfileUpdate

router = APIRouter()


@router.get("/@me", response_model=ProfileRead)
def get_current_profile(user: str = Depends(get_user)):
    ...


@router.put("/@me", response_model=ProfileRead)
def update_current_profile(user: str = Depends(get_user), *, profile: ProfileUpdate):
    ...


@router.put("/@me/picture", response_model=ProfileRead)
def upload_current_picture(user: str = Depends(get_user), *, picture: UploadFile):
    ...

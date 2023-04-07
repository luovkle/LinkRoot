from fastapi import APIRouter, Depends, Path
from pymongo.database import Database

from app.api.deps import get_user, get_db
from app.schemas.link import LinkCreate, LinkRead, LinkUpdate
from app.schemas.message import Message
from app.crud.link import crud_link

router = APIRouter()


@router.post("/@me", response_model=LinkRead)
def create_link(
    user: str = Depends(get_user), db: Database = Depends(get_db), *, link: LinkCreate
):
    return crud_link.create(db, user, link)


@router.get("/@me", response_model=list[LinkRead])
def get_current_links(user: str = Depends(get_user), db: Database = Depends(get_db)):
    return crud_link.read_many(db, user)


@router.get("/@me/{id}", response_model=LinkRead)
def get_current_link(
    user: str = Depends(get_user),
    db: Database = Depends(get_db),
    *,
    id: str = Path(title="Link ID")
):
    return crud_link.read_one(db, user, id)


@router.put("/@me/{id}", response_model=LinkRead)
def update_current_link(
    user: str = Depends(get_user),
    db: Database = Depends(get_db),
    *,
    id: str = Path(title="Link ID"),
    link: LinkUpdate
):
    return crud_link.update(db, user, id, link)


@router.delete("/@me/{id}", response_model=Message)
def delete_current_link(
    user: str = Depends(get_user),
    db: Database = Depends(get_db),
    *,
    id: str = Path(title="Link ID")
):
    return crud_link.delete(db, user, id)

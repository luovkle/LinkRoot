from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pymongo.database import Database

from app.schemas.link import Link, LinkCreate, LinkUpdate
from app.core.config import settings


class CRUDLink:
    def _get_by_user(self, db: Database, user: str):
        return list(db.links.find({"user": user}).limit(settings.CRUD_LINKS_LIMIT))

    def _get_by_id(self, db: Database, user: str, id: str):
        doc = db.links.find_one({"user": user, "_id": id})
        if not doc:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return doc

    def _allow_new_doc(self, db: Database, user: str):
        return (
            False
            if db.links.count_documents({"user": user}) >= settings.CRUD_LINKS_LIMIT
            else True
        )

    def create(self, db: Database, user: str, link: LinkCreate):
        if not self._allow_new_doc(db, user):
            raise HTTPException(
                status.HTTP_403_FORBIDDEN, "Maximum number of elements reached"
            )
        link_db = jsonable_encoder(Link.parse_obj(link))
        id = db.links.insert_one({"user": user, **link_db}).inserted_id
        return self._get_by_id(db, user, id)

    def read_one(self, db: Database, user: str, id: str):
        return self._get_by_id(db, user, id)

    def read_many(self, db: Database, user: str):
        return self._get_by_user(db, user)

    def update(self, db: Database, user: str, id: str, link: LinkUpdate):
        doc = self._get_by_id(db, user, id)
        changes = db.links.update_one(
            {"user": user, "_id": id}, {"$set": link.dict(exclude_none=True)}
        ).modified_count
        return self._get_by_id(db, user, id) if changes else doc

    def delete(self, db: Database, user: str, id: str):
        doc = self._get_by_id(db, user, id)
        db.links.delete_one({"user": user, "_id": doc["_id"]})
        return {"msg": "ok"}


crud_link = CRUDLink()

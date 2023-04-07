from fastapi import UploadFile, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pymongo.database import Database

from app.schemas.profile import Profile, ProfileUpdate
from app.utils.picture import update_picture
from app.utils.profile import get_data


class CRUDProfile:
    def _get_data(self, access_token):
        data = get_data(access_token)
        if not data:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return data["name"], data["picture"]

    def _create(self, db: Database, user: str, access_token: str):
        name, picture = self._get_data(access_token)
        user_db = jsonable_encoder(
            Profile(**{"user": user, "name": name, "picture_url": picture})
        )
        id = db.profiles.insert_one(user_db).inserted_id
        return db.profiles.find_one({"_id": id})

    def _get_by_user(self, db: Database, user: str, access_token: str):
        doc = db.profiles.find_one({"user": user})
        if not doc:
            doc = self._create(db, user, access_token)
            if not doc:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
        return doc

    def read(self, db: Database, user: str, access_token: str):
        return self._get_by_user(db, user, access_token)

    def update(
        self, db: Database, user: str, profile: ProfileUpdate, access_token: str
    ):
        doc = self._get_by_user(db, user, access_token)
        changes = db.profiles.update_one(
            {"user": user}, {"$set": profile.dict(exclude_none=True)}
        ).modified_count
        return self._get_by_user(db, user, access_token) if changes else doc

    def update_picture(
        self, db: Database, user: str, picture: UploadFile, access_token: str
    ):
        doc = self._get_by_user(db, user, access_token)
        res = update_picture(picture, doc["picture_id"])
        if res.get("error"):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, res["error"])
        url = res["secure_url"]
        changes = db.profiles.update_one(
            {"user": user},
            {"$set": {"picture_url": url}},
        ).modified_count
        return self._get_by_user(db, user, access_token) if changes else doc


crud_profile = CRUDProfile()

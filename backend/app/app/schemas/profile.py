from uuid import uuid4

from pydantic import BaseModel, Field, HttpUrl


class ProfileBase(BaseModel):
    name: str
    bio: str | None = None


class Profile(ProfileBase):
    id: str = Field(default_factory=uuid4, alias="_id")
    picture_id: str = Field(default_factory=uuid4)
    picture_url: HttpUrl
    user: str


class ProfileRead(ProfileBase):
    picture_url: HttpUrl


class ProfileUpdate(BaseModel):
    name: str | None = None
    bio: str | None = None

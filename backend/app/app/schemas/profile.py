from uuid import uuid4

from pydantic import BaseModel, Field, HttpUrl


class ProfileBase(BaseModel):
    user: str
    bio: str


class Profile(ProfileBase):
    id: str = Field(default_factory=uuid4, alias="_id")
    picture_id: str = Field(default_factory=uuid4)
    picture_url: HttpUrl | None = None


class ProfileRead(ProfileBase):
    id: str = Field(alias="_id")
    picture_url: HttpUrl


class ProfileUpdate(BaseModel):
    user: str | None = None
    bio: str | None = None

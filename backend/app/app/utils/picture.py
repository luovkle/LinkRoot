import cloudinary
import cloudinary.uploader
import cloudinary.exceptions
from fastapi import UploadFile

cloudinary.config(secure=True)


def update_picture(picture: UploadFile, id: str):
    try:
        res = cloudinary.uploader.upload(picture.file, public_id=id, overwrite=True)
    except cloudinary.exceptions.Error as e:
        res = {"error": str(e)}
    return res

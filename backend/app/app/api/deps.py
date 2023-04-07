from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from app.utils.jwt import VerifyToken
from app.db.client import client

token_auth_scheme = HTTPBearer()


def verify_token(token: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("msg", "")
        )
    return result


def get_user(token: dict = Depends(verify_token)):
    return token["sub"]


def get_db():
    return client.app


def get_access_token(request: Request):
    return request.headers["Authorization"].split()[1]

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from app.utils.jwt import VerifyToken

token_auth_scheme = HTTPBearer()


def verify_token(token: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("msg", "")
        )
    return result

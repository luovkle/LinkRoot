import requests

from app.core.config import settings


def get_data(access_token: str):
    res = requests.get(
        settings.AUTH0_ISSUER + "userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return res.json() if res.status_code == 200 else None

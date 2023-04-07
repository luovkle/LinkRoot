import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    APP_LICENSE_NAME: str = "MIT"
    APP_LICENSE_URL: str = "https://opensource.org/licenses/MIT"
    CORS_ORIGINS: list[str] = ["http://127.0.0.1:3000", "http://localhost:3000"]
    MIDDLEWARE_ALLOW_CREDENTIALS: bool = True
    MIDDLEWARE_ALLOW_METHODS: list[str] = ["*"]
    MIDDLEWARE_ALLOW_HEADERS: list[str] = ["*"]
    API_V1_STR: str = "/api/v1"

    # DB
    DB_URI: str = os.getenv("DB_URI", "")

    # AUTH0
    AUTH0_DOMAIN: str = os.getenv("DOMAIN", "")
    AUTH0_API_AUDIENCE: str = os.getenv("API_AUDIENCE", "")
    AUTH0_ISSUER: str = os.getenv("ISSUER", "")
    AUTH0_ALGORITHMS: str = os.getenv("ALGORITHMS", "")

    # CRUD
    CRUD_LINKS_LIMIT: int = 10


settings = Settings()

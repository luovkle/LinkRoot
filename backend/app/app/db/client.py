from pymongo import MongoClient

from app.core.config import settings

client = MongoClient(settings.DB_URI)

from pymongo import MongoClient

from core.config import settings


client = MongoClient(settings.ATLAS_URI)
db = client.get_database(settings.DB_NAME)


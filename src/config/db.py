from pymongo import MongoClient
from .config import get_config

_client = None

def init_db():
    global _client
    if _client is not None:
        return
    config = get_config()
    _client = MongoClient(config.mongo.uri)

def get_db():
    if _client is None:
        raise RuntimeError("DB not initialized")
    config = get_config()
    return _client[config.mongo.db_name]
import os
from .base import AppConfig, MongoConfig, RedisConfig, KafkaConfig

def get_dev_config() -> AppConfig:
    mongo_uri = os.environ.get("MONGO_URI")
    mongo_db = os.environ.get("MONGO_DB", "appdb")

    if not mongo_uri:
        raise RuntimeError("MONGO_URI is required")
    
    return AppConfig(
        env="dev",
        debug=True,
        mongo=MongoConfig(uri=mongo_uri, db_name=mongo_db),
        redits=RedisConfig(url=os.environ.get("REDIS_URL")),
        kafka=KafkaConfig(
            bootstrap_servers=os.environ.get("KAFKA_BOOTSTRAP_SERVERS"),
            client_id=os.environ.get("KAFKA_CLIET_ID"),
        ),
    )
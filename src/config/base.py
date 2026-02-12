from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class MongoConfig:
    uri: str
    db_name: str


@dataclass(frozen=True)
class RedisConfig:
    uri: Optional[str] = None


@dataclass(frozen=True)
class KafkaConfig:
    bootstrap_servers: Optional[str] = None
    client_id: Optional[str] = None

@dataclass(frozen=True)
class AppConfig:
    env: str
    debug: bool
    mongo: MongoConfig
    redis: RedisConfig
    kafka: KafkaConfig



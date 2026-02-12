import os
from .dev import get_dev_config

def get_config():
    env = os.environ.get("APP_NEW", "dev").lower()

    if env == "dev":
        return get_dev_config()
    
    raise RuntimeError(f"Unsupported APP_ENV: {env}")
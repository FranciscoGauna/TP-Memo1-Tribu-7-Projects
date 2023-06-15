from dotenv import dotenv_values
from src.logger import logger

configurations = {
    "test": {
        "ENV": "test",
        "HOST": "0.0.0.0",
        "PORT": 35000,
        "TESTING": True,
        "DB": "memory"
    },
    "dev": {
        "ENV": "dev",
        "HOST": "0.0.0.0",
        "PORT": 35000,
        "TESTING": True,
        "DB": "mongo"
    },
    "prod": {
        "ENV": "prod",
        "HOST": "0.0.0.0",
        "PORT": 80,
        "TESTING": False,
        "DB": "mongo"
    },
}

env_vals = dotenv_values(".env")

if "MODE" in env_vals:
    configurations.setdefault('missing_key', configurations["dev"])  # Devuelve el conf de default por las dudas
    config = configurations[env_vals["ENV"]]
else:
    config = configurations["dev"]

for k, v in env_vals.items():
    config[k] = v

if "LOGGER_LEVEL" in config:
    try:
        logger.set_level(config["LOGGER_LEVEL"])
    except KeyError:
        logger.error("LOGGER_LEVEL .env key doesn't match a correct level")
logger.info(f"Loaded .env variables {list(env_vals.keys())}")



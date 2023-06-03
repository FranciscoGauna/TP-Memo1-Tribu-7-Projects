from src.database.mongo import MongoDB
from src.conf import config


def get_database():
    if config["DB"] == "mongo":
        return MongoDB(config["MONGO_URL"], config["MONGO_USER"], config["MONGO_PASS"])

    raise Exception("DB not found")

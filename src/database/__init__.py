from src.database.mongo import MongoDB
from src.database.memory import MemoryDB
from src.conf import config


def get_database():
    if config["DB"] == "memory":
        return MemoryDB()
    if config["DB"] == "mongo":
        return MongoDB(config["MONGO_URL"], config["MONGO_USER"], config["MONGO_PASS"])

    raise Exception("DB not found")

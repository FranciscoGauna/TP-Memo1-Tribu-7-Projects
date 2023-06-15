from src.database.mongo import MongoDB
from src.database.memory import MemoryDB
from src.conf import config


database = None


def get_database():
    global database
    if database is None:
        if config["DB"] == "memory":
            database = MemoryDB()
        if config["DB"] == "mongo":
            database = MongoDB(config["MONGO_URL"], config["MONGO_USER"], config["MONGO_PASS"])

    return database

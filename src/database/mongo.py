from typing import List

from pymongo import MongoClient


# Singleton
from src.logger import logger


class MongoDB:
    def __init__(self, url, user, password):
        uri = f"mongodb+srv://{user}:{password}@{url}/?retryWrites=true&w=majority"
        self.client = MongoClient(host=uri)
        self.db = self.client.projects

        try:
            self.client.admin.command('ping')
            logger.info("Successfully connected to database")
        except Exception as e:
            logger.error(f"Error connecting to database {e}")
            raise e

    def get(self, collection, obj_filter) -> List[object]:
        return list(self.db[collection].find(obj_filter))

    def save(self, collection, obj):
        return self.db[collection].insert_one(obj)

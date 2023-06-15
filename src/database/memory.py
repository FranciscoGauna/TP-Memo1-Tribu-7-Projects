from typing import List
from pymongo_inmemory import MongoClient

from src.logger import logger


# Singleton
class MemoryDB:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.projects


    def get(self, collection, obj_filter) -> List[object]:
        return list(self.db[collection].find(obj_filter))

    def save(self, collection, obj):
        res = self.db[collection].insert_one(obj)
        if not res.acknowledged:
            raise Exception("Insertion Failed")
        return res.inserted_id

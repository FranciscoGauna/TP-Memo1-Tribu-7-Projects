from typing import List
from pymongo_inmemory import MongoClient

from src.logger import logger


# Singleton
class MemoryDB:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.projects


    def save(self, collection, obj):
        res = self.db[collection].insert_one(obj)
        if not res.acknowledged:
            raise Exception("Insertion Failed")
        return res.inserted_id

    def get(self, collection, obj_filter) -> List[object]:
        return list(self.db[collection].find(obj_filter))

    def update(self, collection, obj_filter, obj):
        return self.db[collection].update_one(obj_filter, obj)

    def delete(self, collection, obj_filter):
        return self.db[collection].delete_one(obj_filter)
from typing import Dict, List

from bson import ObjectId

from src.model.project import Project
from src.database import get_database
from src.model.task import Task

db = get_database()
collection = "projects"


def save_task(pid, task):
    db.update(collection, {"_id": ObjectId(pid)}, {"$push": {"tasks": task}})

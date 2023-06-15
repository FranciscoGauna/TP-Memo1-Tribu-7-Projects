from bson import ObjectId

from src.database import get_database
from src.service.projects import retrieve_project

db = get_database()
collection = "projects"


def save_task(pid, task, task_id):
    db.update(collection, {"_id": ObjectId(pid)}, {"$set": {"tasks": {task_id: task}}})


def retrieve_task(pid, tid):
    project = retrieve_project(pid)
    return project["tasks"][tid]


def remove_task(pid, task_id):
    db.update(collection, {"_id": ObjectId(pid)}, {"$unset": {f"tasks.{task_id}": ""}})

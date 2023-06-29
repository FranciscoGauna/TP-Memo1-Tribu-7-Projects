from bson import ObjectId

from src.database import get_database
from src.service.projects import retrieve_project

db = get_database()
collection = "projects"


def create_task_id(project):
    task_id = ObjectId()
    while task_id in project["tasks"]:
        task_id = ObjectId()
    return task_id


def save_task(pid, task, task_id=None):
    project = retrieve_project(pid)
    if task_id is None:
        task_id = str(create_task_id(project))
    tasks = project["tasks"]
    tasks[task_id] = task
    db.update(collection, {"_id": ObjectId(pid)}, {"$set": {"tasks": tasks}})
    return task_id


def retrieve_task(pid, tid):
    project = retrieve_project(pid)
    task = project["tasks"][tid]
    task["puid"] = tid
    return task


def remove_task(pid, task_id):
    db.update(collection, {"_id": ObjectId(pid)}, {"$unset": {f"tasks.{task_id}": ""}})

from typing import Dict, List

from bson import ObjectId

from src.model.project import Project
from src.database import get_database
from src.model.task import Task

db = get_database()
collection = "projects"


def parse_id(db_res: Dict):
    db_res["uid"] = str(db_res.pop("_id"))
    return db_res


def save_project(project_json) -> str:
    return db.save(collection, project_json)


def retrieve_project(uid):
    results = db.get(collection, {"_id": ObjectId(uid)})
    return list(map(parse_id, results))[0]


def retrieve_projects() -> List[Dict]:
    return list(map(parse_id, db.get(collection, {})))


def update_project(uid, project_json):
    return db.update(collection, {"_id": ObjectId(uid)}, {"$set": project_json})


def remove_project(uid) -> bool:
    return db.delete(collection, {"_id": ObjectId(uid)})

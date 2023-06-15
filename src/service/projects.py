from typing import Dict, List

from src.model.project import Project
from src.database import get_database
from src.model.task import Task

db = get_database()
collection = "projects"



def parse_task(task_dict):
    return Task(
        task_dict["state"],
        task_dict["stage"],
        task_dict["stages"]
    )


def parse_project(project_dict):
    return Project(
        project_dict["name"],
        project_dict["client"],
        project_dict["start_date"],
        project_dict["end_date"],
        project_dict["project_leader"],
        project_dict["development_team"],
        list(map(parse_task, project_dict["tasks"])),
    )


def parse_id(db_res: Dict):
    db_res["uid"] = str(db_res.pop("_id"))
    return db_res


def list_projects() -> List[Dict]:
    return list(map(parse_id, db.get(collection, {})))


def save_project(project: Project) -> bool:
    return db.save(collection, project)

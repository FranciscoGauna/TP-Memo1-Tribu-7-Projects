from typing import Dict

from src.model.project import Project
from src.database import get_database

db = get_database()
collection = "projects"


def dict_projects() -> Dict[str, Project]:
    projects = map(lambda x: Project(x["name"]), db.get(collection, {}))
    return dict(map(lambda x: (x.name, x), projects))


def save_project(project: Project) -> bool:
    if len(db.get(collection, {"name": project.name})) > 0:
        return False

    db.save(collection, project)
    return True

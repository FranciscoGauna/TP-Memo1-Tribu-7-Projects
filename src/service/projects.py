from typing import Dict

from src.model.project import Project
from src.database import get_database

db = get_database()
collection = "projects"


def list_projects() -> Dict[str, Project]:
    return db.get(collection, {})


def save_project(project: Project) -> bool:
    db.save(collection, project)
    return True

from src.service.projects import list_projects, save_project
from src.model.project import Project
from src.model.task import Task


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


def get_projects():
    return list_projects()


def insert_projects(project_json):
    return save_project(parse_project(project_json))

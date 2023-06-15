from src.service.projects import retrieve_project, update_project, retrieve_projects, save_project, remove_project
from src.model.project import Project
from src.model.task import Task


def parse_task(task_dict):
    return Task(
        task_dict["id"],
        task_dict["state"],
        task_dict["name"],
        task_dict["start_date"],
        task_dict["end_date_est"],
        task_dict["hours_est"]
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


def post_project(project_json):
    return save_project(project_json)


def get_project(uid):
    return retrieve_project(uid)


def get_projects():
    return retrieve_projects()


def put_project(uid, project_json):
    return update_project(uid, project_json)


def delete_project(uid):
    return remove_project(uid)

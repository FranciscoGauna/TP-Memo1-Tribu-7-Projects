from src.model.project import Project
from src.service.projects import retrieve_project, update_project, retrieve_projects, save_project, remove_project


def post_project(project_json):
    return save_project(Project(**project_json))


def get_project(uid):
    return retrieve_project(uid)


def get_projects():
    return retrieve_projects()


def put_project(uid, project_json):
    return update_project(uid, project_json)


def delete_project(uid):
    return remove_project(uid)

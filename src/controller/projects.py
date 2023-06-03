from src.service.projects import dict_projects, save_project
from src.model.project import Project


def get_projects():
    return dict_projects()


def insert_projects(name):
    return save_project(Project(name))

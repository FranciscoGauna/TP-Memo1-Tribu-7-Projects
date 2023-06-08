from src.service.projects import list_projects, save_project
from src.model.project import Project
from src.model.task import Task
from src.model.risk import Risk


def parse_project(project_dict):
    return Project(
        project_dict["name"],
        project_dict["client"],
        project_dict["start_date"],
        project_dict["end_date"],
        project_dict["project_leader"],
        project_dict["development_team"],
        project_dict["tasks"],
        project_dict["risks"]
    )


def parse_task(task_dict):
    return Task(
        task_dict["state"],
        task_dict["stage"],
        task_dict["stages"]
    )


def parse_risk(risk_dict):
    return Risk(
        risk_dict["title"],
        risk_dict["responsable"],
        risk_dict["probability"],
        risk_dict["impact_level"],
        risk_dict["mitigation_plan"],
        risk_dict["contingency_plan"]
    )


def get_projects():
    return list(map(parse_project, list_projects()))


def insert_projects(name, client, start_date, end_date, project_leader, development_team, tasks, risks):
    tasks = list(map(parse_task, tasks))
    risks = list(map(parse_risk, risks))
    return save_project(Project(name, client, start_date, end_date, project_leader, development_team, tasks, risks))

from typing import List
import datetime

from src.model.task import Task
from src.model.risk import Risk


class Project(dict):
    name: str
    client: str
    start_date: datetime
    end_date: datetime
    project_leader: str
    development_team: List[str]
    tasks: List[Task]
    risks: List[Risk]


    def __init__(self, name, client, start_date, end_date, project_leader, development_team, tasks, risks):
        super().__init__(self, name=name, client=client, start_date=start_date, end_date=end_date,
                         project_leader=project_leader, development_team=development_team, tasks=tasks, risks=risks)
        self.name = name
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.project_leader = project_leader
        self.development_team = development_team
        self.tasks = tasks
        self.risks = risks

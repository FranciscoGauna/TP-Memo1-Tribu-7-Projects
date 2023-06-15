from typing import List
import datetime

from src.model.task import Task


class Project(dict):
    uid: str
    name: str
    client: str
    start_date: datetime
    end_date: datetime
    project_leader: str
    development_team: List[str]
    tasks: List[Task]


    def __init__(self, name, client, start_date, end_date, project_leader, development_team, tasks, uid=None):
        super().__init__(self, name=name, client=client, start_date=start_date, end_date=end_date,
                         project_leader=project_leader, development_team=development_team, tasks=tasks, uid=uid)
        self.name = name
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.project_leader = project_leader
        self.development_team = development_team
        self.tasks = tasks
        self.uid = uid

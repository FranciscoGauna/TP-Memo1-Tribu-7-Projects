from typing import List
import datetime

from src.model.task import Task


class Project(dict):
    uid: str
    name: str
    description: str
    stage: str
    project_leader: str
    tasks: List[Task]
    estimated_hours: float
    start_date: datetime
    end_date: datetime


    def __init__(self, name, description, stage, start_date, end_date,
                 project_leader, estimated_hours, tasks, uid=None):
        super().__init__(self, name=name, description=description, stage=stage, start_date=start_date,
                         end_date=end_date, project_leader=project_leader, estimated_hours=estimated_hours,
                         tasks=tasks, uid=uid)
        self.name = name
        self.description = description
        self.stage = stage
        self.start_date = start_date
        self.end_date = end_date
        self.project_leader = project_leader
        self.estimated_hours = estimated_hours
        self.tasks = tasks
        self.uid = uid

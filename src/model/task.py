from typing import List


class Task(dict):
    puid: str
    name: str
    description: str
    state: str
    human_resource: str
    estimated_hours: str
    start_date: str
    end_date: str

    def __init__(self, state, name, description, start_date, end_date, estimated_hours, human_resource="",
                 puid=None):
        super().__init__(self, puid=puid, description=description, state=state, name=name, start_date=start_date,
                         human_resource=human_resource, end_date=end_date, estimated_hours=estimated_hours)
        self.puid = puid
        self.state = state
        self.name = name
        self.description = description
        self.human_resource = human_resource
        self.estimated_hours = estimated_hours
        self.start_date = start_date
        self.end_date = end_date

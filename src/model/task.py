from typing import List


class Task(dict):
    puid: str
    name: str
    description: str
    state: str
    estimated_hours: str
    start_date: str
    end_date_est: str

    def __init__(self, state, name, description, start_date, end_date_est, estimated_hours, puid=None):
        super().__init__(self, puid=puid, description=description, state=state, name=name, start_date=start_date,
                         end_date_est=end_date_est, estimated_hours=estimated_hours)
        self.puid = puid
        self.state = state
        self.name = name
        self.description = description
        self.estimated_hours = estimated_hours
        self.start_date = start_date
        self.end_date_est = end_date_est

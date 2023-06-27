from typing import List


class Task(dict):
    puid: str
    name: str
    description: str
    state: str
    hours_est: str
    start_date: str
    end_date_est: str

    def __init__(self, state, name, description, start_date, end_date_est, hours_est, puid=None):
        super().__init__(self, puid=puid, state=state, name=name, start_date=start_date, end_date_est=end_date_est,
                         hours_est=hours_est)
        self.puid = puid
        self.state = state
        self.name = name
        self.description = description
        self.hours_est = hours_est
        self.start_date = start_date
        self.end_date_est = end_date_est

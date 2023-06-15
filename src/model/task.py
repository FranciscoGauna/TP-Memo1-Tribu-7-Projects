from typing import List


class Task(dict):
    puid: str
    state: str
    name: str
    start_date: str
    end_date_est: str
    hours_est: str

    def __init__(self, puid, state, name, start_date, end_date_est, hours_est):
        super().__init__(self, puid=puid, state=state, name=name, start_date=start_date, end_date_est=end_date_est,
                         hours_est=hours_est)
        self.puid = puid
        self.state = state
        self.name = name
        self.start_date = start_date
        self.end_date_est = end_date_est
        self.hours_est = hours_est

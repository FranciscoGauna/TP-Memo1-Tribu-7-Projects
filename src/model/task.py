from typing import List


class Task(dict):
    state: str
    stage: str
    stages: List[str]

    def __init__(self, state, stage, stages):
        super().__init__(self, state=state, stage=stage, stages=stages)
        self.state = state
        self.stage = stage
        self.stages = stages

from typing import List


class Risk(dict):
    title: str
    responsible: str
    probability: float
    impact_level: str
    mitigation_plan: str
    contingency_plan: str

    def __init__(self, title, responsible, probability, impact_level, mitigation_plan, contingency_plan):
        super().__init__(self, title=title, responsible=responsible, probability=probability,
                         impact_level=impact_level, mitigation_plan=mitigation_plan, contingency_plan=contingency_plan)
        self.title = title
        self.responsible = responsible
        self.probability = probability
        self.impact_level = impact_level
        self.mitigation_plan = mitigation_plan
        self.contingency_plan = contingency_plan

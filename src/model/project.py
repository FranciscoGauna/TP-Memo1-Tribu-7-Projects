class Project(dict):
    def __init__(self, name):
        super().__init__(self, name=name)
        self.name = name

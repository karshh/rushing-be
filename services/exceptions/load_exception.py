class LoadException(Exception):

    def __init__(self, idx, variable):
        self.idx = idx
        self.variable = variable
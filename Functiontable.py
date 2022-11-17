class Functiontable(object):

    def __init__(self):
        self.table = {}

    def populatetable(self,var,expression):
        self.table[var] = expression

class Symboltable:

    
    def __init__(self):
        self.table  = {}
            

    def populatetable(self,var,expr):
        self.table[var] = expr



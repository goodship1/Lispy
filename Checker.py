from Symboltable import Symboltable
class Typechecker:


    def __init__(self):
        self.table = Symboltable()
    
    
    def exprtype(self,expr,op,args,table= None):
        if expr == "exprterm" and op == "\\":
            check = self.dividezero(args)
            if check == False:
                return True
            else:
                return False
        
        if expr == "assigndiv" and op == "\\":
            check = self.dividezero(args)
            if check == False:
                return True
            else:
                return False

        if expr == "exprid" and op == "-":
            check = self.checkvariables(args,table)
            if check == True:
                return True
            else:
                return False

        if expr == "exprid" and op == "*":
            check = self.checkvariables(args,table)
            if check == True:
                return True
            else:
                return False



        
        if expr == "exprid" and op == "+":
            check = self.checkvariables(args,table)
            if check == True:
                return True
            else:
                False


    def checkvariables(self,expr,table):
        id_one =  expr[0].split(" ")[1]
        id_two  = expr[1].split(" ")[1]
        try:
            if id_one in table and id_two in table:
                return True
        except Exception as e:
            return "variable not defined"
            

    def negativeroot(self,expr):
        return expr[0] >= 0


    def dividezero(self,expr):

         if int(expr[1]) == 0:
            raise TypeError("divide by zero error")
         else:
             return False


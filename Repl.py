from Parser import parser
from Lexer import scanner
from Interperter import Interperter

class Replit:
    
    def __init__(self):
        self.interperter = Interperter()
    

    def eval_term_expression(self,expression):
        if expression.leaf == "+":
            print(self.interperter.ast_add(expression.child))
        if expression.leaf == "-":
            print(self.interperter.ast_minus(expression.child))
        if expression.leaf == "*":
            print(self.interperter.ast_times(expression.child))
        if expression.leaf == "\\":
            print(self.interperter.ast_divide(expression.child))
        if expression.leaf == "cos":
            print(self.interperter.ast_cos(expression.child))
        if expression.leaf == "sin":
            print(self.interperter.ast_sin(expression.child))
        if expression.leaf == "!":
            print(self.interperter.ast_factorial(expression.child))
        if expression.leaf == "^":
            print(self.interperter.ast_power(expression.child))
        if expression.leaf == ">":
            print(self.interperter.ast_greaterthan(expression.child))
        if expression.leaf == "<":
            print(self.interperter.ast_lessthan(expression.child))
        if expression.leaf == ">=":
            print(self.interperter.ast_greaterthaneq(expression.child))
        if expression.leaf == "<=":
            print(self.interperter.ast_lessthaneq(expression.child))
        
    def eval_trig_expressions(self,expr,op):
        print(op,expr)
        print(self.interperter.ast_term_trig_term(expr,op))
    
    def eval_expression_id(self,expression,op):
        if op  == "+":
            print(self.interperter.ast_id_plus_id(expression))
        if op == "-":
            print(self.interperter.ast_id_minus_id(expression))
        if op == "*":
            print(self.interperter.ast_id_times_id(expression))
        if op == "\\":
            print(self.interperter.ast_id_divide_id(expression))
        if op == "^":
            id_one  = expression[0].split(" ")[1]
            id_two = expression[1].split(" ")[1]
            try:
               first=self.interperter.table.table[id_one]
               second=self.interperter.table.table[id_two]
               print(int(first) ** int(second))
            except Exception as e:
                print("variable not defined")
            


    
    def variable_display(self,variable):
        var = variable[0] 
        display = self.interperter.table.table[str(variable[0])]
        show = "{var} -> {value}".format(var = var,value = display)
        print(show)
    

    def repl(self):
        while True:
            commands = input("#")
            res = parser.parse(commands)
            try:
                if res.op == "assignid":
                     program = self.interperter.program.append(commands)
                     self.interperter.run_parser(program)
                     self.interperter.visitnodes()
                     self.variable_display(res.child)
                self.interperter.parse.append(res)
                if res.op == "assignplus":
                        self.interperter.visitnodes()
                        self.variable_display(res.child)
                if res.op == "assignminus":
                        self.interperter.visitnodes()
                        self.variable_display(res.child)
                if res.op == "assigntimes":
                        self.interperter.visitnodes()
                        self.variable_display(res.child)
                if res.op == "assigngreaterthan":
                        self.interperter.visitnodes()
                        self.variable_display(res.child)
                if res.op == "assignlessthan":
                        self.interperter.visitnodes()
                        self.variable_display(res.child)
                if res.op == "exprterm":
                        self.eval_term_expression(res)
                if res.op == "assignlessthaneq":
                        self.interperter.visitnodes()
                        self.variable_display(res.child)
                if res.op == "assigngreaterthaneq":
                        self.interperter.visitnodes()
                        self.variable_display(res.child)
                if res.op == "exprid":
                        self.interperter.visitnodes()
                        self.eval_expression_id(res.child,res.leaf)
                

                if res.op == "exprtrigterm":
                        self.interperter.visitnodes()
                        print(res.child,res.leaf)
                        self.eval_trig_expressions(res.child,res.leaf)
                          
                if res.op == "assignpower":
                        self.interperter.visitnodes()
                        self.variable_display(res.child)

            except Exception as e:
                print(" ")

repl = Replit()
repl.repl()

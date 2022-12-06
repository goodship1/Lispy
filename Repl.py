from Parser import parser
from Lexer import tokens
from Interperter import Interperter

class Replit:
    
    def __init__(self):
        self.interperter = Interperter()
        self.table  = {}

    

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
        if expression.leaf == "%":
            try:
                print(int(expression.child[0]) % int(expression.child[1]))
            except Exception as e:
                print("syntax error")

        
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
    
    def display_variable(self,variable):
        value = self.interperter.table.table[variable]
        show = "{var} -> {value}".format(var = variable,value = value)
        print(show)


    

    def repl(self):
        check = []
        while True:
            commands = input("#")
            prog =  parser.parse(commands)
            if prog != None: 
                if prog.op == "exprterm":
                    self.eval_term_expression(prog)
                
                if prog.op == "assignplus":
                   self.interperter.parse.append(prog)
                   nodes=self.interperter.visitnodes()
                   self.interperter.runprogram(nodes)
                   variable  = prog.child[0]
                   self.display_variable(variable)
                
                if prog.op == "assignminus":
                    self.interperter.parse.append(prog)
                    nodes = self.interperter.visitnodes()
                    self.interperter.runprogram(nodes)
                    variable = prog.child[0]
                    self.display_variable(variable)
                
                if prog.op == "assigntimes":
                    self.interperter.parse.append(prog)
                    nodes = self.interperter.visitnodes()
                    variable = prog.child[0]
                    self.display_variable(variable)
                
                if prog.op == "assigndiv":
                    
                    zero_check =  int(prog.child[2]) == int(0)
                    if zero_check == True:
                        print("syntax error")
                    else:
                        self.interperter.parse.append(prog)
                        nodes  = self.interperter.visitnodes()
                        variable = prog.child[0]
                        self.display_variable(variable)
                
                if prog.op == "assigngreater":
                    self.interperter.parse.append(prog)
                    nodes = self.interperter.visitnodes()
                    variable =  prog.child[0]
                    self.display_variable(variable)

                if prog.op == "assignlessthan":
                    self.interperter.parse.append(prog)
                    nodes =  self.interperter.visitnodes()
                    variable = prog.child[0]
                    self.display_variable(variable)

                if prog.op == "assigngreatereq":
                    self.interperter.parse.append(prog)
                    nodes = self.interperter.visitnodes()
                    variable =  prog.child[0]
                    self.display_variable(variable)
                
                if prog.op == "assignlessthaneq":
                    self.interperter.parse.append(prog)
                    nodes =  self.interperter.visitnodes()
                    variable = prog.child[0]
                    self.display_variable(variable)

                if prog.op == "list-define":
                    self.interperter.parse.append(prog)
                    nodes  = self.interperter.visitnodes()
                    variable = prog.child[0]
                    self.display_variable(variable)
                
                if prog.op == "mod-term":
                   self.eval_term_expression(prog)

                if prog.op == "cons-terms":
                    self.interperter.parse.append(prog)
                    self.interperter.visitnodes()
                
                if prog.op == "map-list":
                    self.interperter.parse.append(prog)
                    self.interperter.visitnodes()

                  
repl = Replit()
repl.repl()

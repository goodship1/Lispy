from Parser import parser
from Symboltable import Symboltable
from Ast import Node
from Checker import Typechecker
import sys
import math
from Functiontable import Functiontable

class Interperter:
    
    def __init__(self):
        self.program = []
        self.line_number=0
        self.typechecker = Typechecker()
        self.table =  Symboltable()
        self.parse = []
        self.function =  Functiontable()


    def  read_file(self):
        args  = sys.argv
        open_file =  args[1]
        with open(open_file) as read:
            for line in read.readlines():
                    if line!="\n":
                        self.program.append(line.strip())

        self.run_parser(self.program)

    def run_parser(self,program):
        for operations in self.program:
            res = parser.parse(operations)
            self.parse.append(res)
            
            
    def ast_add(self,add):
        return int(add[0]) + int(add[1])
    
    def ast_minus(self,minus):
        return int(minus[0]) - int(minus[1])

    def ast_times(self,times):
        return  int(times[0]) * int(times[1])

    def ast_divide(self,divide):
        try:
            return int(divide[0]) / int(divide[1])
        except Exception as  e:
            return "Syntax error zero divisor"
    
    def ast_cos(self,cos):
        return math.cos(int(cos[0]))

    def ast_sqrt(self,sqrt):
        return math.sqrt(int(sqrt[0]))

    def ast_greaterthan(self,greaterthan):
        return int(greaterthan[0]) > int(greaterthan[1])
    
    
    def ast_power(self,power):
        return math.pow(int(power[0]),int(power[1]))


    def ast_lessthan(self,lessthan):
        return int(lessthan[0]) < int(lessthan[1])
    
    def ast_lessthaneq(self,lessthaneq):
        return int(lessthaneq[0]) <= int(lessthaneq[1])

    def ast_greaterthaneq(self,greaterthaneq):
        return int(greaterthaneq[0]) >= int(greaterthaneq[1])

    def ast_factorial(self,factorial):
        factor = int(factorial[0])
        result = 1
        if factor > 1:
            for calculate in range(1,factor+1):
                result = result * calculate
        return result
    
    def ast_factorial_id(self,factorial):
        id_one = factorial[0].split(" ")[1]
        id_two = factorial[0].split(" ")[1]
        expression =  [id_one,id_two]
        check = self.checkexpression(expression) 
        if check == True:
            result = 1
            factor = int(self.table.table[id_one])
            if factor > 1:
                for calculate in range(1,factor+1):
                    result = result * calculate
                return result
        else:
            raise NameError("Incompatiable types")


         
    def extractvariables(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        return [id_one,id_two]

    def symboltablecheck(self,variables):
        try:
            if variables[0] in self.table.table and variables[1] in self.table.table:
                return True
        except Exception as e:
            raise NameError("variable not  defined")

    
    def ast_id_times_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            return int(self.table.table[id_one])*int(self.table.table[id_two])
        else:
            raise NameError("Incompatiable Types")

     

    def ast_id_minus_id(self,expr):
        id_one =  expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expressions = [id_one,id_two]
        check = self.checkexpression(expressions)
        if check == True:
            return int(self.table.table[id_one]) - int(self.table.table[id_two])
        else:
            raise NameError("Imcompatiable types")


    
    def checkexpression(self,var):
        store = []
        for x in var:
            s = self.table.table[x]
            store.append(s)
        for x in store:
            s = type(x)
            if s == bool:
                return False
        return True

        


    def ast_id_divide_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            return int(self.table.table[id_one]) / int(self.table.table[id_two])
        else:
            raise NameError("divide by zero")

        

    def ast_id_greaterthan_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            return int(self.table.table[id_one]) > int(self.table.table[id_two])
        else:
            raise NameError("Incompatiable types")

    
    def ast_id_greaterthaneq_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            return int(self.table.table[id_one]) >= int(self.table.table[id_two])
        else:
            raise NameError("Incompatiable types")
    

    def ast_id_lessthaneq_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            return int(self.table.table[id_one]) <= int(self.table.table[id_two])
        else:
            raise NameError("Incompatiable types")

    
    def ast_id_lessthan_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            return int(self.table.table[id_one]) < int(self.table.table[id_two])
        else:
            raise NameError("Incompatitable types")

    def ast_id_plus_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expressions = [id_one,id_two]
        check =  self.checkexpression(expressions)
        if check == True:
            return int(self.table.table[id_one]) + int(self.table.table[id_two])
        else:
            raise NameError("Incompatiable types")
        
    
    def ast_id_power_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            first = int(self.table.table[id_one])
            second = int(self.table.table[id_two])
            return first**second
        else:
            raise NameError("Incompatiable types")

    def ast_sin_id(self,expr):
        id_one = expr[1].split(" ")[1]
        id_two = expr[0].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            return math.sin(self.table.table[id_one])
        else:
            raise NameError("Incompatitable types")

    def ast_cos_id(self,expr):
        id_one = expr[0].split(" ")[1]
        id_two = expr[1].split(" ")[1]
        expression = [id_one,id_two]
        check = self.checkexpression(expression)
        if check == True:
            return math.cos(self.table.table[id_two])
        else:
            raise NameError("Incompatiable types")
    

    def ast_id_op_term(self,expression,op):
        variable = expression[0].split(" ")[1]
        id_one = self.table.table[variable]
        expressions = [variable,variable]
        check = self.checkexpression(expressions)
        if check == True:
            if op == "+":
                return int(id_one) + int(expression[1])
            if op == "-":
                return int(id_one) - int(expression[1])
            if op == "*":
                return int(id_one) * int(expression[1])
            if op == "\\":
                try:
                    return  int(id_one) / int(expressions[1])
                except Exception as e:
                    raise NameError("zero divisor")
            if op == ">":
                return int(id_one) > int(expression[1])
            if op == "<":
                return int(id_one) < int(expression[1])
            if op == ">=":
                return int(id_one) >= int(expression[1])

            if op == "<=":
                return int(id_one) <= int(expression[1])
            if op == "^":
                return int(id_one) ** int(expression[1])

    def ast_sin(self,sin):
        return math.sin(int(sin[0]))

    def ast_if_greaterthan_assign(self,expr):
        #(define id if > 20 20  then else)

        if_state = expr[1]
        then_state = expr[2]
        else_state = expr[3]
        if int(if_state[1]) > int(if_state[2]):
            if then_state[0] == "+":
                return int(then_state[1]) + int(then_state[2])
            if then_state[0] == "-":
                return int(then_state[1]) - int(then_state[2])
            if then_state[0] == "*":
                return int(then_state[1]) * int(then_state[2])
        else:
            if else_state[0] == "+":
                return int(else_state[1]) + int(else_state[2])
            if else_state[0] == "-":
                return int(else_state[1]) - int(else_state[2])
            if else_state[0] == "*":
                return int(else_state[1]) * int(else_state[2])
           
    def ast_if_lessthan_assign(self,expr):
      if_state = expr[1]
      then_state = expr[2]
      else_state = expr[3]
      if int(if_state[1]) < int(if_state[2]):
          if then_state[0] == "+":
              return int(then_state[1]) + int(then_state[2])
          if then_state[0] == "-":
              return int(then_state[1]) - int(then_state[2])
          if then_state[0] == "*":
              return int(then_state[1]) * int(then_state[2])
      else:
        if else_state[0] == "+":
            return int(else_state[1]) + int(else_state[2])
        if else_state[0] == "-":
            return int(else_state[1]) - int(else_state[2])
        if else_state[0] == "*":
            return int(else_state[1]) * int(else_state[2])

    def assignment_if_check(self,expr):
        compare = expr[0][1:]
        then =  expr[1][1:]
        last = expr[2][1:]
        expression = []
        variable_lookup = []
        variables = [compare,then,last]
        for var in variables:
             extract = self.extractvariables(var)
             expression.append(extract)
        for check  in expression:
            s = self.symboltablecheck(check)
            variable_lookup.append(s)
        check = [True , True,True] == variable_lookup
        if check == True:
            return  True
        else:
            raise NameError("Variable not defined")
		
    
    
    
    def ast_if_lessthaneq_assign(self,expr):
        if_state = expr[1]
        then_state = expr[2]
        else_state = expr[3]
        if int(if_state[1]) <= int(if_state[2]):
            if then_state[0] == "+":
                return int(then_state[1]) + int(then_state[2])
            if then_state[0] == "-":
                return int(then_state[1]) - int(then_state[2])
            if then_state[0] == "*":
                return int(then_state[1]) * int(then_state[2])
        else:
            if else_state[0] == "+":
                return int(else_state[1]) + int(else_state[2])
            if else_state[0] == "-":
                return int(else_state[1]) - int(else_state[2])
            if else_state[0] == "*":
                return int(else_state[1]) - int(else_state[2])
    
    def ast_term_trig_term(self,expr,op):
        if expr[1] == "cos" and op == "+":
            cos_term = math.cos(int(expr[2]))
            return int(expr[0]) + cos_term
        if expr[1] == "sin" and op == "+":
            sin_term = math.sin(int(expr[2]))
            return int(expr[0]) + sin_term
        if expr[1] == "cos" and op == "*":
            cos_term = math.cos(int(expr[2]))
            return int(expr[0]) * cos_term
        if expr[1] == "sin" and op == "*":
            sin_term = math.sin(int(expr[2]))
            return int(expr[0]) * sin_term
        if expr[1] == "cos" and op == "-":
            cos_term = math.cos(int(expr[2]))
            return int(expr[0]) - cos_term
        



    def ast_if_greaterthaneq_assign(self,expr):
        if_state = expr[1]
        then_state = expr[2]
        else_state = expr[3]
        if int(if_state[1]) >= int(if_state[2]):
            if then_state[1] == "+":
                return int(then_state[1]) + int(then_state[2])
            if then_state[1] == "-":
                return int(then_state[1]) - int(then_state[2])
            if then_state[1] == "*":
                return int(then_state[1]) * int(then_state[2])
        else:
            if else_state[0] == "+":
                return int(else_state[1]) + int(else_state[2])
            if else_state[0] == "-":
                return int(else_state[1]) - int(else_state[2])
            if else_state[0] == "*":
                return int(else_state[1]) * int(else_state[2])
    
    def ast_assign_if_id(self,expr):
        
        if_state = expr[0]
        then_state = expr[1]
        last = expr[2]
        if_var_one = if_state[1].split(" ")[1]
        if_var_two = if_state[2].split(" ")[1]
        then_var_one = then_state[1].split(" ")[1]
        then_var_two = then_state[2].split(" ")[1]
        last_var_one = last[1].split(" ")[1]
        last_var_two = last[1].split(" ")[1]
        
        if if_state[0] == ">":
            check = int(self.table.table[if_var_one]) > int(self.table.table[if_var_two])
            if check == True:
                if then_state[0] == "+":
                    return int(self.table.table[then_var_one]) + int(self.table.table[then_var_two])
                if then_state[0] == "-":
                    return int(self.table.table[then_var_one]) - int(self.table.table[then_var_two])
                if then_state[0] == "*":
                    return int(self.table.table[then_var_one]) * int(self.table.table[then_var_two])
            else:
                if last[0] == "+":
                    return int(self.table.table[last_var_one]) + int(self.table.table[last_var_two])
                if last[0] == "-":
                    return int(self.table.table[last_var_one]) + int(self.table.table[last_var_two])
                if last[0] == "*":
                    return int(self.table.table[last_var_one]) * int(self.table.table[last_var_two])

        if if_state[0] == "<":
            check = int(self.table.table[if_var_one]) < int(self.table.table[if_var_two])
            if then_state[0] == "+":
                return int(self.table.table[then_var_one]) + int(self.table.table[then_var_two])
            if then_state[0] == "-":
                return int(self.table.table[then_var_one]) + int(self.table.table[then_var_two])
            if then_state[0] == "*":
                return int(self.table.table[then_var_one]) + int(self.table.table[then_var_two])
        else:
            if last[0] == "+":
                return int(self.table.table[last_var_one]) + int(self.table.table[last_var_two])
            if last[0] == "-":
                return int(self.table.table[last_var_one]) - int(self.table.table[last_var_two])
            if last[0] == "*":
                return int(self.table.table[last_var_one]) * int(self.table.table[last_var_two])
        if if_state[0] == ">=":
            check = int(self.table.table[if_var_one]) >= int(self.table.table[if_var_two])
            if check == True:
                if then_state[0] == "+":
                    return int(self.table.table[then_var_one]) + int(self.table.table[then_var_two])
                if then_state[0] == "-":
                    return int(self.table.table[then_var_one]) - int(self.table.table[then_var_two])
                if then_state[0] == "*":
                    return int(self.table.table[then_var_one]) * int(self.table.table[then_var_two])
            else:
                if last[0] == "+":
                    return int(self.table.table[last_var_one]) + int(self.table.table[last_var_two])
                if last[0] == "*":
                    return int(self.table.table[last_var_one]) * int(self.table.table[last_var_two])
                if last[0] == "-":
                    return int(self.table.table[last_var_one]) - int(self.table.table[last_var_two])
        if if_state[0] == "<=":
            check = int(self.table.table[if_var_one]) <= int(self.table.table[if_var_two])
            if check == True:
                if if_state[0] == "+":
                    return int(self.table.table[then_var_one]) + int(self.table.table[then_var_two])
                if if_state[0] == "-":
                    return int(self.table.table[then_var_one]) - int(self.table.table[then_var_two])
                if if_state[0] == "*":
                    return int(self.table.table[then_var_one]) * int(self.table.tabe[then_var_two])
            else:
                if last[0] == "+":
                   return int(self.table.table[last_var_one]) + int(self.table.table[last_var_two])
                if last[0] == "-":
                   return int(self.table.table[last_var_one]) - int(self.table.table[last_var_two])
                if last[0] == "*":
                    return int(self.table.table[last_var_one]) * int(self.tabe.table[last_var_two])
    


    def ast_list_terms(self,expression):
        new_list = list(expression[1])
        return new_list

 

    def ast_list_op_id(self,expr,op):
        variable =  expr[1].split(" ")[1]
        data =  self.table.table[variable]
        check =  type(data) == type([])
        if op == "first" and len(data) >=1:
            try:
                return data[0]
            except Exception as e:
                raise NameError("incompatiable type")
        if op  == "second"  and len(data)>=2:
            try:
                return data[1]
            except Exception as e:
                raise NameError("incompatiable type")
        if op  == "third" and len(data)>=3:
            try:
                return data[2]
            except Exception as e:
                raise NameError("incompatiable type")
        if op == "fourth" and len(data)>=4:
            try:
                return data[3]
            except Exception as e:
                raise NameError("incompatiable type")
        if op == "fifth" and len(data)>=5:
            try:
                return data[4]
            except Exception as e:
                raise NameError("incompataible type")
        if op == "sixth" and len(data)>=6:
            try:
                return data[5]
            except Exception as e:
                raise NameError("incompatiable type")
        if op == "seventh" and len(data)>=7:
            try:
                return data[6]
            except Exception as e:
                raise NameError("incompatabile type")
        if op == "eighth" and len(data)>=8:
            try:
                return data[8]
            except Exception as e:
                raise NameError("incompatiable type")
        if op == "nineth" and len(data)>=9:
            try:
                return data[9]
            except Exception as e:
                raise NameError("incompataible type")
        if op == "tenth" and len(data)>=10:
            try:
                return data[10]
            except Exception as e:
                raise NameError("incompatiable type")
        else:
            raise NameError("Invalid index")


    def ast_list_op_terms(self,expression,op):
        try:
          if op == "first":
            data =  expression[1]
            return data[1]
          if op == "second":
              data =  expression[1]
              return data[2]
          if op == "third":
	          data = expression[1]
	          return data[3]
          if op == "fourth":
              data = expression[1]
              return data[4]
          if op == "fifth":
              data = expression[1]
              return data[5]
          if op == "sixth":
            data = expression[1]
            return data[6]
          if op == "seventh":
            data = expression[1]
            return data[7]
          if op == "eighth":
             data = expression[1]
             return data[8]
          if op == "nineth":
            data = expression[1]
            return data[9]
          if op == "tenth":	
           data =  expression[1]
           return data[10]
        except Exception as e:
			      NameError("Element out of bounds")

    def ast_cons_term(self,expression):
        list_one = expression[0]
        list_two =  expression[1]
        new_list = []
        for item in list_one:
            new_list.append(int(item))
        for item in list_two:
            new_list.append(int(item))
        return new_list


    def ast_cons_id_id(self,expression):
        id_one = self.table.table[expression[0].split(" ")[1]]
        id_two = self.table.table[expression[1].split(" ")[1]]
        if type(id_one) == type([]) and type(id_two) == type([]):
            new_list = []
            for items in id_one:
                new_list.append(int(items))
            for items in id_two:
                new_list.append(int(items))
            return new_list
        else:
            raise NameError("Incompatiable types")

        
    def ast_term_id(self,expression,op):
        id_one = expression[1].split(" ")[1]
        variable = self.table.table[id_one]
        print(op)
        if type(variable) != bool and type(variable) != type([]) and type(variable) != str:        
            if op == "+":
                return int(self.table.table[id_one]) + int(expression[0])
            if op == "-":
                return int(self.table.table[id_one]) - int(expression[0])
            if op == "*":
                return int(self.table.table[id_one])  * int(expression[0])
            if op == "\\":
                if int(self.table.table[id_one]) == 0:
                    raise NameError("Zero divisor")
                else:
                    return int(self.table.table[id_one]) / int(expression[0])
        else:
            raise NameError("Incompatiable type")



    def ast_string_list(self,expression):
        new_list = list(expression[1])
        return new_list
            
    def ast_if_term_term(self,expression):
        if_state = expression[0]
        if_term_one = expression[1]
        if_term_two = expression[2]
        then_term_one = expression[4]
        then_term_two = expression[5]
        else_term_one = expression[7]
        else_term_two = expression[8]
        
        if if_state == "<=":
            check == int(if_term_one) <= int(if_term_two)
            if check == True:
                if expression[3] == "+":
                    return int(then_term_one) + int(then_term_two)
                if expression[3] == "-":
                    return int(then_term_one) - int(then_term_two)
                if expression[3] == "*":
                    return int(then_term_one) * int(then_term_two)

                if expression[3] == "\\":
                    try:
                        return int(then_term_one) / int(then_term_two)
                    except Exception as e:
                        raise NameError("Zero divisor")
            
            else:
                if expression[6] == "+":
                    return int(else_term_one) + int(else_term_two)
                if expression[6] == "-":
                    return int(else_term_one) - int(else_term_two)
                if expression[6] == "*":
                    return int(else_term_one) * int(else_term_two)
                if expression[6] == "\\":
                    try:
                        return int(else_term_one) / int(else_term_two)
                    except Exception as e:
                        raise NameError("Zero divisor")


        if if_state == ">=":
            check = int(if_term_one) >= int(if_term_two)
            if check == True:
                if expression[3] == "+":
                    return int(then_term_one) + int(then_term_two)
                if expression[3] == "-":
                    return int(then_term_one) - int(then_term_two)
                if expression[3] == "*":
                    return int(then_term_one) * int(then_term_two)
                if expression[3] == "\\":
                    try:
                        return int(then_term_one) / int(then_term_two)
                    except Exception as e:
                        raise NameError("Zero divisor")
            else:
                if expression[6] == "+":
                    return int(else_term_one) + int(else_term_two)
                if expression[6] == "-":
                    return int(else_term_one) - int(else_term_two)
                if expression[6] == "*":
                    return int(else_term_one) * int(else_term_two)
                if expression[6] == "\\":
                    try:
                        return int(else_term_one) / int(else_term_two)
                    except Exception as e:
                        raise NameError("Zero divisor")
                    

        if if_state == "<":
            check  = int(if_term_one) < int(if_term_two)
            if check == True:
                if expression[3] == "+":
                    return int(then_term_one) + int(then_term_one)
                if expression[3] == "-":
                    return int(then_term_one) - int(then_term_two)
                if expression[3] == "*":
                    return int(then_term_one) * int(then_term_two)
                if expression[3] == "\\":
                    try:
                        return int(then_term_one) / int(then_term_two)
                    except Exception as e:
                        raise NameError("Zero divisor")

            else:
                if expression[6] == "+":
                    return int(else_term_one) + int(else_term_two)
                if expression[6] == "-":
                    return int(else_term_one) - int(else_term_two)
                if expression[6] == "*":
                    return int(else_term_one) * int(else_term_two)
                if expression[6] == "\\":
                    try:
                        return int(else_term_one) / int(else_term_two)
                    except Exception as e:
                        raise NameError("Zeo divisor")


        if if_state == ">":
            check = int(if_term_one) > int(if_term_two)
            if check == True:
                if expression[3] == "+":
                    return int(then_term_one) + int(then_term_two)
                if expression[3] == "*":
                    return int(then_term_one) * int(then_term_one)
                if expression[3] == "-":
                    return int(then_term_one) - int(then_term_one)

                if expression[3] == "\\":
                    try:
                        return int(then_term_one) / int(then_term_two)
                    except Exception as e:
                        raise NameError("Zero divisor")
            else:
                if expression[6] == "+":
                    return int(else_term_one) + int(else_term_two)
                if expression[6] == "-":
                    return int(else_term_one) - int(else_term_two)
                if expression[6] == "*":
                    return int(else_term_one) * int(else_term_two)
                if expression[6] ==  "\\":
                    try:
                        return int(else_term_one) / int(else_term_two)
                    except Exception as e:
                        NameError("Zero divisor")
    




    def ast_define_cons_terms(self,expressions):
       
        list_one =  expressions[1]
        list_two =  expressions[2]
        new_list = []
        for items in list_one:
            new_list.append(int(items))
        for items in list_two:
            new_list.append(int(items))
        return new_list
    

    def functiontablecheck(self,variable):
        if self.function.table[variable]:
            return True
        else:
            raise NameError("function not define")
        




    def ast_list_op_strings(self,expression,op):
        list_define = expression[1]
        if op == "first":
            return list_define[0]
        if op == "second":
            try:
                return list_define[2]
            except Exception as e:
                raise NameError("Index not in bounds")
        if op == "third":
            try:
                return list_define[3]
            except Exception as e:
                raise NameError("Index not in bounds")
        if op == "fourth":
            try:
                return list_define[4]
            except Exception as e:
                raise NameError("Index not in bounds")
        if op == "fifth":
            try:
                return list_define[5]
            except Exception as e:
                raise NameError("Index not in bounds")
        if op == "sixth":
            try:
                return list_define[6]
            except Exception as e:
                raise NameError("Index not in bounds")
        if op == "seventh":
            try:
                return list_define[7]
            except Exception as e:
                raise NameError("Index not in bounds")
        if op == "eighth":
            try:
                return list_define[8]
            except Exception as e:
                raise NameError("Index not in bounds")
        if op == "nineth":
            try:
                return list_define[9]
            except Exception as e:
                raise NameError("Index not in bounds")
        if op == "tenth":
            try:
                return list_define[10]
            except Exception as e:
                raise NameError("Index not in bounds")
    
    def ast_term_mod_term(self,expression):
        variable_one  = int(expression[0])
        variable_two =  int(expression[1])
        if variable_two == 0:
            raise NameError("Zero divisor")
        return variable_one % variable_two



    def ast_map_list(self,expression):
        list_one  = expression[1]
        list_two  = expression[2]
        new_list =  None
        return_list = []
        length_list_one =  len(list_one)
        length_list_two =  len(list_two)
        print(length_list_one < length_list_two)
        if length_list_one == length_list_two:
            new_list = list(zip(list_one,list_two))
            if expression[0] == "+":
                for items in range(len(new_list)):
                    result =  int(new_list[items][0]) + int(new_list[items][1])
                    return_list.append(result)
            if expression[0] == "-":
                for items in range(len(new_list)):
                    result =  int(new_list[items][0]) - int(new_list[items][1])
                    return_list.append(result)
            if expression[0] == "*":
                for items in range(len(new_list)):
                    result  = int(new_list[items][0]) * int(new_list[items][1])
                    return_list.append(result)
            if expression[0] == "\\":
                for items in range(len(new_list)):
                    try:
                        result  = int(new_list[items][0]) / int(new_list[items][1])
                        return_list.append(result)
                    except Exception as e:
                        raise NameError("Zero divisor")
            return return_list

        if length_list_one > length_list_two:
            extend_by  = length_list_one - length_list_two
            if expression[0] == "+":
                 add_to  = [0] * extend_by
                 list_two  = list_two + add_to
                 new_list = list(zip(list_one,list_two))
                 for items in range(len(new_list)):
                     result = int(new_list[items][0]) +  int(new_list[items][1])
                     return_list.append(result)
            
            if expression[0] == "-":
                 add_to = [0] * extend_by
                 list_two  = list_two+add_to
                 new_list = list(zip(list_one,list_two))
                 for items in range(len(new_list)):
                     result = int(new_list[items][0]) - int(new_list[items][1])
                     return_list.append(result)

            if expression[0] == "*":
                add_to = [1] * extend_by
                list_two =  list_two + add_to
                new_list =  list(zip(list_one,list_two))
                for items in range(len(new_list)):
                    result = int(new_list[items][0]) * int(new_list[items][1])
                    return_list.append(result)
            
            if expression[0] == "\\":
                add_to =  [1] * extend_by
                list_two = list_two + add_to
                new_list  = list(zip(list_one,list_two))
                for items in range(len(new_list)):
                    try:
                        result = int(new_list[items][0]) / int(new_list[items][1])
                        return_list.append(result)
                    except Exception as e:
                        raise NameError("Zero divisor")
            return return_list
           
                
        if  length_list_one < length_list_two:
                extend_by  = length_list_one - length_list_two
                if expression[0] == "+":
                    add_to = [0] * extend_by
                    list_one = list_one + add_to
                    new_list = list(zip(list_one,list_two))
                    for items in range(len(new_list)):
                        result =  int(new_list[items][0]) + int(new_list[items][1])
                        return_list.append(result)

                if expression[0] == "-":
                    add_to = [0] * extend_by
                    list_one  = list_one + add_to
                    new_list =  list(zip(list_one,list_two))
                    for items in range(len(new_list)):
                        result = int(new_list[items][0]) - int(new_list[items][1])
                        return_list.append(result)
                
                if expression[0] == "*":
                    add_to = [1] * extend_by
                    list_one = list_one + add_to
                    new_list =  list(zip(list_one,list_two))
                    for items in range(len(new_list)):
                        result = int(new_list[items][0]) * int(new_list[items][1])
                        return_list.append(result)
               
                if expression[0] == "\\":
                   add_to = [1] * extend_by
                   list_one = list_one + add_to
                   new_list = list(zip(list_one,list_two))
                   for items in range(len(new_list)):
                       try:
                           result =  int(new_list[items][0]) / int(new_list[items][1])
                           return_list.append(result)
                       except Exception as e:
                          raise NameError("Zero divisor error")
                return return_list
               


    def ast_func_exprid(self,expression,op):
        if op == "+":
            try:
                add = []
                for items in expression:
                    add.append(int(items))
                result = 0
                for items in add:
                    result+=items
                return result
            except Exception as e:
                raise NameError("Incompatiable types")
        if op == "-":
            try:
                minus = []
                for items in expression:
                    minus.append(int(items))
                result = minus[0]
                for items in minus:
                    result-= items
                return result
            except Exception as e:
                raise NameError("Incompatiable types")
        if op == "*":
            try:
                times = []
                for items in expression:
                    times.append(int(items))
                result = times[0]
                for items in times:
                    result*=items
                return result
            except Exception as e:
                raise NameError("Incompatiable types")
        if op == ">":
            try:
                greaterthan = []
                for items in expression:
                    greaterthan.append(int(items))
                result = greaterthan[0]
                compare = []
                for items in greaterthan:
                    if result>items:
                        compare.append(True)
                    else:
                        compare.append(False)
                if False in compare:
                    return False
                else:
                    return True
            except Exception as e:
                raise NameError("Incompatiable types")
        if op == "<=":
            try:
                lessthaneq = []
                for items in expression:
                    lessthaneq.append(int(items))
                result = lessthaneq[0]
                compare = []
                for items in lessthaneq:
                    if result <= items:
                        compare.append(True)
                    else:
                        compare.append(False)
                if False in compare:
                    return False
                else:
                    return True
            except Exception as e:
                raise NameError("Incompatiable types")
        if op == ">=":
            try:
                greaterthaneq = []
                for items in expression:
                    greaterthaneq.append(int(terms))
                result = greaterthaneq[0]
                compare = []
                for items in greaterthaneq:
                    if result <= items:
                        compare.append(True)
                    else:
                        compare.append(False)
                if False in compare:
                    return False
                else:
                    return True
            except Exception as e:
                raise NameError("Incompatiable types")
    

    def ast_search_terms(self,expression):
        get_list = self.table.table[expression[0]]
        truth_list = [True]*len(expression[1])
        compare = []
        for items in expression[1]:
            if items in get_list:
                compare.append(True)
        return len(compare) == len(truth_list)

    
    def ast_search_strings(self,expression):
        get_list = self.table.table[expression[0]]
        truth_list = [True] * len(expression[1])
        compare = []
        for items in expression[1]:
            if items in get_list:
                compare.append(True)
        return len(compare) == len(truth_list)
        



    def ast_search_args(self,expression):
        get_list  = self.table.table[expression[0]]
        truth_list =  [True] * len(expression[1])
        arg_list = []
        args =  expression[1]
        compare = []
        for items in args:
            try:
                arg = self.table.table[items]
                arg_list.append(items)
            except Exception as e:
                raise NameError("Variable not defined")
        if len(arg_list) == len(truth_list):
            for items in arg_list:
                if str(self.table.table[items]) in get_list:
                    compare.append(True)

        return len(compare)  == len(truth_list)







    def visitnodes(self):
        
        program = []
        for instructions in self.parse:
            if instructions.op == "exprterm" and instructions.leaf == "+":
                add =  self.ast_add(instructions.child)
                program.append(add)
            if instructions.op == "exprterm" and instructions.leaf == "-":
                minus = self.ast_minus(instructions.child)
                program.append(minus)
            if instructions.op == "exprterm" and instructions.leaf == "\\":
                div_zero = self.typechecker.exprtype(instructions.op,instructions.leaf,instructions.child)
                if div_zero:
                   div = self.ast_divide(instructions.child)
                   program.append(div)
            if instructions.op == "exprterm" and instructions.leaf == "*":
                times =  self.ast_times(instructions.child)
                program.append(times)
            if instructions.op == "assignplus" and instructions.leaf == "+":
                variable  = instructions.child[0]
                add = self.ast_add(instructions.child[1:])
                self.table.populatetable(variable,add)
                self.typechecker.table.table = self.table.table
            if instructions.op == "assignminus" and instructions.leaf == "-":
                variable = instructions.child[0]
                minus = self.ast_minus(instructions.child[1:])
                self.table.populatetable(variable,minus)
                self.typechecker.table = self.table.table
            if instructions.op == "assigntimes" and instructions.leaf == "*":
                variable = instructions.child[0]
                times = self.ast_times(instructions.child[1:])
                self.table.populatetable(variable,times)
                self.typechecker.table.table = self.table.table
            if instructions.op == "assigndiv" and instructions.leaf == "\\":
                div_zero =  self.typechecker.exprtype(instructions.op,instructions.leaf,instructions.child[1:])
                if div_zero:
                    variable = instructions.child[0]
                    divide = self.ast_divide(instructions.child[1:])
                    self.table.populatetable(variable,divide)
            if instructions.op == "assigngreater" and instructions.leaf == ">":
                variable = instructions.child[0]
                greaterthan = self.ast_greaterthan(instructions.child[1:])
                self.table.populatetable(variable,greaterthan)
            if instructions.op == "assigngreatereq" and instructions.leaf == ">=":
                variable = instructions.child[0]
                greaterthaneq = self.ast_greaterthaneq(instructions.child[1:])
                self.table.populatetable(variable,greaterthaneq)
            if instructions.op == "assignlessthan" and instructions.leaf == "<":
                variable = instructions.child[0]
                lessthan = self.ast_lessthan(instructions.child[1:])
                self.table.populatetable(variable,lessthan)
            if instructions.op == "assignlessthaneq" and instructions.leaf == "<=":
                variable = instructions.child[0]
                lessthaneq = self.ast_lessthaneq(instructions.child[1:])
                self.table.populatetable(variable,lessthaneq)
            if instructions.op == "assignpower" and instructions.leaf == "^":
                variable = instructions.child[0]
                power = self.ast_power(instructions.child[1:])
                self.table.populatetable(variable,power)

            if instructions.op == "exprid" and instructions.leaf == "+":
                variables  = self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    add = self.ast_id_plus_id(instructions.child)
                    program.append(add)
            if instructions.op == "exprid" and instructions.leaf == "-":
                variables = self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    minus = self.ast_id_minus_id(instructions.child)
                    program.append(minus)
            if instructions.op == "exprid" and instructions.leaf == "*":
                variables = self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    times =  self.ast_id_times_id(instructions.child)
                    program.append(times)
            if instructions.op == "exprid" and instructions.leaf == ">":
                variables =  self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    greaterthan = self.ast_id_greaterthan_id(instructions.child)
                    program.append(greaterthan)
            if instructions.op == "exprid" and instructions.leaf == "<":
                variables = self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    lessthan = self.ast_id_lessthan_id(instructions.child)
                    program.append(lessthan)
            if instructions.op == "exprid" and instructions.leaf == ">=":
                variables = self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    greaterthaneq = self.self.ast_id_greaterthaneq_id(instructions.child)
                    program.append(greaterthaneq)
            if instructions.op == "exprid" and instructions.leaf == "<=":
                variables  = self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    lessthaneq = self.ast_id_lessthaneq_id(instructions.child)
                    program.append(lessthaneq)
            if instructions.op == "exprterm" and instructions.leaf == "!":
                factorial =  self.ast_factorial(instructions.child)
                program.append(factorial)
            
            if instructions.op == "exprid" and instructions.leaf == "!":
                variables =  self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    factorial = self.ast_factorial_id(instructions.child)
                    program.append(factorial)
            if instructions.op == "exprid" and instructions.leaf == "^":
                variables =  self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    power = self.ast_id_power_id(instructions.child)
                    program.append(power)
            if instructions.op == "exprid" and instructions.leaf == "sin":
                variables  = self.extractvariables(instructions.child)
                check = self.symbotablecheck(variables)
                if check == True:
                    sin = self.ast_sin_id(instructions.child)
                    program.append(sin)

            if instructions.op == "exprid" and instructions.leaf == "cos":
                variables = self.extractvariable(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    cos = self.ast_cos_id(instructions.child)
                    program.append(cos)
            
            if instructions.op == "assignid" and instructions.leaf == "=":
                if instructions.child[1][0] == ">": 
                    assign = self.ast_if_greaterthan_assign(instructions.child)
                    variable =  instructions.child[0]
                    self.table.populatetable(variable,assign)
                if instructions.child[1][0] == "<":
                    assign = self.ast_if_lessthan_assign(instructions.child)
                    variable = instructions.child[0]
                    self.populatetable(variable,assign)
                if instructions.child[1][0] == "<=":
                    assign = self.ast_if_lessthaneq_assign(instructions.child)
                    variable = instructions.child[0]
                    self.populatetable(variable,assign)
                if instructions.child[1][0] == ">=":
                    assign = self.ast_if_greaterthaneq_assign(instructions.child)
                    variable = instructions.child[0]
                    self.populatetable(variabe,assign)
            
            if instructions.op == "assignmentifid" and instructions.leaf[0] == "=":
                     check = self.assignment_if_check(instructions.child)
                     if check == True:
                         variable =  instructions.leaf[1]
                         assignment_if_id =  self.ast_assign_if_id(instructions.child)
                         self.table.populatetable(variable,assignment_if_id)
            
            if instructions.op == "exprid" and instructions.leaf[0] == "\\":
                variables =  self.extractvariables(instructions.child)
                check = self.symboltablecheck(variables)
                if check == True:
                    divide =  self.ast_id_divide_id(instructions.child)
                    program.append(divide)
            
            if instructions.op == "exprtrigterm":
                trigterm = self.ast_term_trig_term(instructions.child,instructions.leaf)
                program.append(trigterm)
            

            if instructions.op == "ifterm":
                ifterm = self.ast_if_term_term(instructions.child)
                program.append(ifterm)

            if instructions.op == "idtermop":
                variables = [instructions.child[0],instructions.child[0]]
                lookup =  self.extractvariables(variables)
                check = self.symboltablecheck(lookup)
                if check == True:
                    op = self.ast_id_op_term(instructions.child,instructions.leaf)
                    program.append(op)

            if instructions.op == "list-string-term":
                create_string_list =  self.ast_string_list(instructions.child)

            if instructions.op == "list-term":
                create_list = self.ast_list_terms(instructions.child)
            
            if instructions.op == "string-list-define":
                variable =  instructions.child[0]
                list_define =  list(instructions.child[1])
                self.table.populatetable(variable,list_define)
            
            if instructions.op == "string-list-op":
                list_op = self.ast_list_op_strings(instructions.child,instructions.leaf)
                program.append(list_op)

            if instructions.op == "search-terms":
                variable = instructions.child[0]
                if  self.table.table[variable]:
                    check = self.table.table[variable]
                    if type(check) == type([]):
                        terms =  self.ast_search_terms(instructions.child)
                        program.append(terms)
                    else:
                        raise NameError("Not of type list")
            
            if instructions.op == "search-args":
                variable =  instructions.child[0]
                if self.table.table[variable]:
                    check =  self.table.table[variable]
                    if type(check) == type([]):
                        args = self.ast_search_args(instructions.child)
                        program.append(args)
                    else:
                        raise NameError("Not of type list")

            if instructions.op == "search-strings":
                variable =  instructions.child[0]
                if self.table.table[variable]:
                    check = self.table.table[variable]
                    if type(check) == type([]):
                        strings =  self.ast_search_args(instructions.child)
                        program.append(strings)
                    else:
                        raise NameError("Not of type list")


            
            if instructions.op == "cons-define":
                variable = instructions.child[0]
                cons_define = self.ast_define_cons_terms(instructions.child)
                self.table.populatetable(variable,cons_define)
            
            if instructions.op == "function-define":
                function_name = instructions.child[0]
                expr  = instructions.child[2]
                self.function.populatetable(function_name,expr)


            if instructions.op == "list-define":
                variable = instructions.child[0]
                list_define  = list(instructions.child[2])
                self.table.populatetable(variable,list_define)

            if instructions.op == "list-id-op":
                variables = [instructions.child[1],instructions.child[1]]
                lookup = self.extractvariables(variables)
                check =  self.symboltablecheck(lookup)
                list_op =  self.ast_list_op_id(instructions.child,instructions.leaf)
                program.append(list_op)

            if instructions.op == "strdefine":
                variable = instructions.child[0]
                self.table.populatetable(variable,str(instructions.child[1]))

            if instructions.op =="function-call":
                if self.function.table[instructions.child[0]]:
                   op = self.function.table[instructions.child[0]]
                   if op.op == "exprid":
                      func = self.ast_func_exprid(instructions.child[1],op.leaf)
                      program.append(func)
            
            if instructions.op == "mod-term":
                mod = self.ast_term_mod_term(instructions.child)
                program.append(mod)

            if instructions.op == "mod-id":
                variable = instructions.child[0]
                mod = self.ast_term_mod_term(instructions.child[1:])
                self.table.populatetable(variable,mod)

            if instructions.op == "map-list":
                map_list = self.ast_map_list(instructions.child)
                print(map_list)

            if instructions.op == "map-define":
                variable = instructions.child[0]
                instructions.child = instructions.child[1:]
                map_list = self.ast_map_list(instructions.child)
                self.table.populatetable(variable,map_list)
                    
            if instructions.op == "list":
                list_op = self.ast_list_op_terms(instructions.child,instructions.leaf)
                program.append(list_op)

            if instructions.op == "cons-terms":
                cons = self.ast_cons_term(instructions.child)
                print(cons)
            if instructions.op == "cons-id-list":
                variables =  [instructions.child[0],instructions.child[1]]
                lookup =  self.extractvariables(variables)
                check =  self.symboltablecheck(lookup)
                cons_id_term =  self.ast_cons_id_id(instructions.child)
                print(cons_id_term)

            if instructions.op == "exprtermid":
                variables = [instructions.child[1], instructions.child[1]]
                lookup = self.extractvariables(variables)
                check = self.symboltablecheck(lookup)
                term_id = self.ast_term_id(instructions.child,instructions.leaf)
                program.append(term_id)



        return program
                        
    def runprogram(self,program):
        for instructions in program:
            print(instructions)







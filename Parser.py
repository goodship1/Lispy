import ply.yacc as yacc
from Lexer import tokens
from Symboltable import Symboltable
from Ast import Node
    
table =  Symboltable()

def p_plus(p):
        #parser rule for (+ term term)
        'expr : opening plus term term closing'
        p[0] = Node("exprterm",[p[3],p[4]],p[2])


def p_divide(p):
    'expr : opening divide term term closing'
    p[0] =  Node("exprterm",[p[3],p[4]],p[2])

def p_divideidid(p):
    'expr : opening divide id id closing'
    id_one = "lookup {id_one}".format(id_one = p[3])
    id_two = "lookup {id_two}".format(id_two = p[4])
    p[0] =  Node("exprid",[id_one,id_two],p[2])




def p_id_compare_term(p):
    '''expr : opening greaterthan id term closing
          | opening greaterthan term id closing
          | opening lessthan term id closing
          | opening lessthan id term closing
          | opening greaterthaneq id term closing
          | opening lessthaneq id term closing
          | opening greaterthaneq term id closing 
        '''
    if p[3] == "term":
	    look_up = "lookup {id_one}".format(id_one = p[4])
	    p[0] = Node("id_compare_term",[p[3] , look_up],p[2])
    else:
        p[0] = Node("id_compare_term",[look_up, p[3] ],p[2])





def p_minus(p):
    'expr : opening minus term term closing'
    p[0] = Node("exprterm",[p[3],p[4]],p[2])

def p_times(p):
    'expr : opening times term term closing'
    p[0] = Node("exprterm",[p[3],p[4]],p[2])

def p_cos(p):
    'expr : opening COS term closing'
    p[0] = Node("exprterm",[p[3],p[3]],"cos")

def p_sin(p):
    'expr : opening SIN term closing'
    p[0] =  Node("exprterm",[p[3],p[3]],"sin")

def p_greaterthan(p):
    #parser rule for (< 100 200) = false 
    'expr : opening greaterthan term term closing'
    p[0] = Node("exprterm",[p[3],p[4]],p[2])

def p_lessthan(p):
    'expr : opening lessthan term term closing'
    p[0] = Node("exprterm",[p[3],p[4]],p[2])

def p_greaterthanequal(p):
    'expr : opening greaterthaneq term term closing'
    p[0] =  Node("exprterm",[p[3],p[4]],p[2])

def p_lessthanequal(p):
    'expr : opening lessthaneq term term closing'
    p[0] = Node("exprterm",[p[3],p[4]],p[2])

def p_sqrt(p):
    'expr : opening SQRT term closing'
    p[0] =  Node("exprterm",[p[4],p[4]],"sqrt")

def p_varplusvar(p):
    'expr : opening plus id id closing'
    id_one = "lookup {id_one}".format(id_one = p[3])
    id_two = "lookup {id_two}".format(id_two = p[4])
    p[0] = Node("exprid",[id_one,id_two],p[2])

def p_ifstatements(p):
    '''expr : opening IF greaterthan term term plus term term plus term term closing
          | opening IF greaterthan term term plus term term minus term term closing
          | opening IF greaterthan term term plus term term times term term closing
          | opening IF greaterthan term term plus term term divide term term closing
          | opening IF greaterthan term term minus term term divide term term closing
          | opening IF lessthan term term plus term term plus term term closing
          | opening IF lessthan term term plus term term minus term term closing
          | opening IF lessthan term term minus term term minus term term closing
          | opening IF lessthan term term minus term term times term term closing
          | opening IF lessthan term term  plus term term times term term closing
          | opening IF greaterthaneq term term  plus term term plus term term closing
          | opening IF greaterthaneq term term minus term term times term term closing
          | opening IF greaterthaneq term term times term term times term term closing
          | opening IF greaterthaneq term term minus term term minus term term closing
          | opening IF lessthaneq term term plus term term plus term term closing
          | opening IF lessthaneq term term plus term term minus term term closing
          | opening IF lessthaneq term term minus term term minus term term closing
          | opening IF lessthaneq term term times term term times term term closing
          '''
    p[0] = Node("ifterm",[p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11]],"if")


def p_term_bin_id(p):
    '''expr : opening plus id term closing
            | opening minus id term closing
            | opening times id term closing
            | opening divide id term closing
            | opening POW id term closing
            '''
    id_one = "lookup {id_one}".format(id_one = p[3])
    if p[2] == "pow":
        p[0] = Node("idtermop",[id_one,p[4]],"^")
    p[0] = Node("idtermop",[id_one,p[4]],p[2])

def p_term_plus_trig(p):
    '''expr : opening plus term COS term closing
            | opening plus term SIN term closing
            | opening minus term SIN term closing
            | opening times term SIN term closing
            | opening times term COS term closing
            | opening minus term COS term closing
            | opening divide term SIN term closing
            | opening divide term COS term closing
            '''
    if p[2] == "+":
        p[0] = Node("exprtrigterm",[p[3],p[4],p[5]],p[2])
    if p[2] == "-":
        p[0] = Node("exprtrgiterm",[p[3],p[4],p[5]],[2])
    if p[2] == "*":
        p[0] = Node("exprtrigterm",[p[3],p[4],p[5]],p[2])
    if p[2] == "\\":
        p[0] = Node("exprtrigterm",[p[3],p[4],p[5]],p[2])



def p_sin_id(p):
    'expr : opening SIN id closing'
    id_one = "lookup {id_one}".format(id_one = p[3])
    p[0] = Node("exprid",[id_one,id_one],"sin")


def p_cos_id(p):
    'expr : opening COS id closing'
    id_one = "lookup {id_one}".format(id_one = p[3])
    p[0] = Node("exprid",[id_one,id_one],"cos")


def p_define_if_greaterthan(p):
    '''expr : opening DEFINE id  IF greaterthan term term  plus term term plus term term closing
              | opening DEFINE id IF greaterthan term term plus term term minus term term closing
              | opening DEFINE id IF greaterthan term term times term term plus term term closing
              | opening DEFINE id IF greaterthan term term times term term times term term closing
              | opening DEFINE id IF greaterthan term term minus term term minus term term closing
              | opening DEFINE id IF lessthan term term plus term term plus term term closing
              | opening DEFINE id IF lessthan term term  plus term term minus term term closing
              | opening DEFINE id IF lessthan term term plus term term times term term closing
              | opening DEFINE id IF lessthan term term minus term term minus term term closing
              | opening DEFINE id IF lessthan term term times term term times term term closing
              | opening DEFINE id IF lessthaneq term term plus term term plus term term closing
              | opening DEFINE id IF lessthaneq term term minus term term minus term term closing
              | opening DEFINE id IF lessthaneq term term times term term times term term closing
              | opening DEFINE id IF lessthaneq term term plus term term  times term term closing

             '''
    p[0] =  Node("assignid",[p[3],[p[5],p[6],p[7]],[p[8],p[9],p[10]],[p[11],p[12],p[13]]],"=")
       


def p_factorial(p):
    'expr : opening FAC term closing'
    p[0] = Node("exprterm" ,[p[3] , p[3]],"!")

def p_factorial_variable(p):
    'expr : opening FAC id closing'
    lookup = "lookup {id_one}".format(id_one =  p[3])
    p[0] =  Node("exprid",[lookup,lookup],"!")
    table.populatetable(p[3],p[0])



def p_varminusvar(p):
    'expr : opening minus id id closing'
    id_one =  "lookup {id_one}".format(id_one = p[3])
    id_two = "lookup {id_two}".format(id_two =  p[4])
    p[0] = Node("exprid",[id_one,id_two],p[2])


def p_vartimesvar(p):
    'expr : opening times id id closing'
    id_one = "lookup {id_one}".format(id_one =  p[3])
    id_two = "lookup {id_two}".format(id_two = p[4])
    p[0] = Node("exprid",[id_one,id_two],p[2])


def p_varlessthanvar(p):
    'expr : opening lessthan id id closing'
    id_one =  "lookup {id_one}".format(id_one =  p[3])
    id_two = "lookup {id_two}".format(id_two  =p[4])
    p[0] =  Node("exprid",[id_one,id_two],p[2])



def p_vargreaterthanvar(p):
    'expr : opening greaterthan id id closing'
    id_one = "lookup {id_one}".format(id_one = p[3])
    id_two  = "lookup {id_two}".format(id_two = p[4])
    p[0] =  Node("exprid",[id_one,id_two],p[2])


def p_varlessthaneqvar(p):
    'expr : opening lessthaneq id id closing'
    id_one = "lookup {id_one}".format(id_one =  p[3])
    id_two = "lookup {id_two)".format(id_two = p[4])
    p[0] = Node("exprid",[id_one,id_two],p[2])


def p_term_op_id(p):
    '''expr : opening plus term id closing
            | opening minus term id closing
            | opening times term id closing
            | opening divide term id closing
            '''
    id_one = "lookup {id_one}".lookup(id_one = p[4])
    p[0] = Node("exprid",[p[3],p[4]],p[2])


def p_vargreaterthanequalvar(p):
    'expr : opening greaterthaneq id id closing'
    id_one  = "lookup {id_one}".format(id_one = p[3])
    id_two  = "lookup {id_two}".format(id_two = p[4])
    p[0] =  Node("exprid",[id_one,id_two],p[2])


def p_powvarvar(p):
    # (pow id id) parser rule
    'expr : opening POW id id closing'
    id_one = "lookup {id_one}".format(id_one  = p[3])
    id_two = "lookup {id_two}".format(id_two =  p[4])
    p[0] =  Node("exprid",[id_one,id_two],"^")




def p_define_varvar(p):
    '''expr : opening DEFINE id IF greaterthan id id plus id id  plus id id closing
            | opening DEFINE id IF greaterthan id id minus id id plus id id closing
            | opening DEFINE id IF greaterthan id id plus id id minus id id closing
            | opening DEFINE id IF greaterthan id id times id id times id id closing
            | opening DEFINE id IF greaterthan id id minus  id id  minus id id closing
            | opening DEFINE id IF greaterthan id id plus id id divide id id closing
            | opening DEFINE id IF greaterthan id id minus id id divide id id closing
            | opening DEFINE id IF greaterthan id id times id id divide id id closing
            | opening DEFINE id IF greaterthan id id  divide id id divide id id closing
            | opening DEFINE id IF lessthan id id plus id id plus id id closing
            | opening DEFINE id IF lessthan id id minus id id plus id id closing
            | opening DEFINE id IF lessthan id id times id id times id id closing
            | opening DEFINE id IF lessthan id id plus id id minus id id closing
            | opening DEFINE id IF lessthan id id plus id id times id id closing
            | opening DEFINE id IF lessthan id id plus id id divide id id closing
            | opening DEFINE id IF lessthan id id minus id id divide id id closing
            | opening DEFINE id IF lessthan id id divide id id divide id id closing
            | opening DEFINE id IF lessthan id id divide id id plus id id closing
            | opening DEFINE id IF greaterthaneq id id plus id id plus id id closing
            | opening DEFINE id IF greaterthaneq id id plus id id minus id id closing
            | opening DEFINE id IF greaterthaneq id id minus id id minus id id closing
            | opening DEFINE id IF greaterthaneq id id times id id times id id closing
            | opening DEFINE id IF greaterthaneq id id times id id plus id id closing
            | opening DEFINE id IF greaterthaneq id id plus id id divide id id closing
            | opening DEFINE id IF greaterthaneq id id divide id id divide id id closing
            | opening DEFINE id IF greaterthaneq id id divide id id minus id id closing
            | opening DEFINE id IF greaterthaneq id id minus id id divide id id closing
            | opening DEFINE id IF lessthaneq  id id plus id id plus id id closing
            | opening DEFINE id IF lessthaneq id id minus id id plus id id closing
            | opening DEFINE id IF lessthaneq id id times id id times id id closing
            | opening DEFINE id IF lessthaneq id id minus id id times id id closing

            '''
    id_one = "lookup {id_one}".format(id_one = p[6])
    id_two = "lookup {id_two}".format(id_two = p[7])
    id_three = "lookup {id_three}".format(id_three =p[9])
    id_four =  "lookup {id_four}".format(id_four = p[10])
    id_five =  "lookup {id_five}".format(id_five = p[12])
    id_six = "lookup {id_six}".format(id_six = p[13])
    p[0] = Node("assignmentifid",[[p[5],id_one,id_two],[p[8],id_three,id_four],[p[11],id_five,id_six]],("=",p[3]))

        


def p_define_var(p):
    '''expr : opening DEFINE id plus term term closing 
              | opening DEFINE id minus term term closing 
              | opening DEFINE id times term term closing 
              | opening DEFINE id divide term term closing 
              | opening DEFINE id greaterthan term term closing
              | opening DEFINE id lessthan term term closing
              | opening DEFINE id greaterthaneq term term closing
              | opening DEFINE id lessthaneq term term closing
              | opening DEFINE id POW term term closing
              '''
    if p[4] == "+":
          p[0] = Node("assignplus",[p[3],p[5],p[6]],p[4])
    if p[4] == "-":
        p[0] = Node("assignminus",[p[3],p[5],p[6]],p[4])
    if p[4] == "*":
        p[0] = Node("assigntimes",[p[3],p[5],p[6]],p[4])
    if p[4] == "\\":
        p[0] = Node("assigndiv",[p[3],p[5],p[6]],p[4])

    if p[4] == ">":
        p[0] = Node("assigngreater",[p[3],p[5],p[6]],p[4])

    if p[4] == ">=":
        p[0] = Node("assigngreatereq",[p[3],p[5],p[6]],p[4])

    if p[4] == "<":
        p[0] = Node("assignlessthan",[p[3],p[5],p[6]],p[4])

    if p[4] == "<=":
        p[0] = Node("assignlessthaneq",[p[3],p[5],p[6]],p[4])

    if p[4] == "pow":
        p[0] = Node("assignpower",[p[3],p[5],p[6]],"^")

    

def p_power_term(p):
    #power rule (pow 2 2)  = 4
    'expr : opening POW term term closing'
    p[0] = Node("exprterm",[p[3],p[4]],'^')


def p_list_term(p):
    '''expr : opening LIST terms closing
            | opening LIST term closing'''
    p[0] = Node("list-term",[p[2],p[3]],"[]")
    


def p_terms(p):
    '''terms  : term
            | term term 
            | term term term 
            | term term term term 
            | term term term term term
            | term term term term term term 
            | term term term term term term term 
            | term term term term term term term term 
            | term term term term term term term term term
            | term term term term term term term term term term 
            '''
    p[0] = []
    try:
        if p[1]:
            p[0].append(p[1])
        if p[2]:
            p[0].append(p[2])
        if p[3]:
            p[0].append(p[3])
        if p[4]:
            p[0].append(p[4])
        if p[5]:
            p[0].append(p[5])
        if p[6]:
            p[0].append(p[6])
        if p[7]:
            p[0].append(p[7])
        if p[8]:
            p[0].append(p[8])
        if p[9]:
            p[0].append(p[9])
        
        if p[10]:
            p[0].append(p[10])

    except Exception  as e:
        p[0]


def p_lists(p):
    'expr : opening DEFINE id LIST terms  closing'
    p[0] = Node("list-define",[p[3],p[4],p[5]],"[id]")


def p_list_varialbe_op(p):
    '''expr : opening FIRST id closing
            | opening SECOND id closing
            | opening THIRD id closing
            | opening FOURTH id closing
            | opening FIFTH id closing
            | opening SIXTH id closing
            | opening SEVENTH id closing
            | opening EIGHTH id closing
            | opening NINETH id closing
            | opening TENTH id closing
            '''
    look_up = "lookup {id_one}".format(id_one = p[3])
    p[0] = Node("list-id-op",[p[2],look_up],p[2])








def p_ops_list(p):
    '''expr : opening FIRST LIST terms closing
          | opening FIRST LIST term closing
          | opening SECOND LIST terms closing
          | opening SECOND LIST term closing
          | opening THIRD LIST terms closing
          | opening FOURTH LIST term closing
          | opening FIFTH LIST terms closing
          | opening SIXTH LIST term closing
          | opening SIXTH LIST terms closing
          | opening EIGHTH LIST term closing
          | opening EIGHTH LIST terms  closing
          | opening NINETH LIST term closing
          | opening NINETH LIST terms closing 
          | opening TENTH LIST term closing
          | opening TENTH LIST terms closing 

          '''
    p[0] = Node("list",[p[2],p[4]],"list")


def p_define_string(p):
    'expr : opening DEFINE id string closing'
    p[0] = Node("strdefine",[p[3],p[4]],"string")


def p_string(p):
    'term : string'
    p[0] = p[1]


def p_term(p):
    'term : integer'
    p[0] = p[1]
   
def p_opening(p):
       'open : opening'
       p[0] = p[1]

def p_error(p):
    print("syntax error")

def p_closing(p):
       'close : closing'
       p[0] = p[1]

def p_args(p):
    '''args : id 
          | id id 
          | id id id 
          | id id id id 
          | id  id id  id id
          | id id id id id id id 
          | id id id id id id id id'''
    p[0] = []
    try:
        if p[1]:
            p[0].append(p[1])
        if p[2]:
            p[0].append(p[2])
        if p[3]:
            p[0].append(p[3])
        if p[4]:
            p[0].append(p[4])
        if p[5]:
            p[0].append(p[5])

        if p[6]:
            p[0].append(p[6])

        if p[7]:
            p[0].append(p[7])

        if p[8]:
            p[0].append(p[8])

        if p[9]:
            p[0].append(p[9])

        if p[10]:
            p[0].append(p[10])
    except Exception as e:
       p[0]




parser = yacc.yacc()


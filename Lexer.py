import ply.lex as scanner
    
keywords = {"set":"SET","union":"UNION","intersectio":"INTERSECTION","exist":"EXIST","print":"PRINT","map":"MAP","defunc":"DEFUNC","cons":"CONS","tenth":"TENTH","nineth":"NINETH","eighth":"EIGHTH","seventh":"SEVENTH","sixth":"SIXTH","fifth":"FIFTH","fourth":"FOURTH","sin":"SIN","cos":"COS","if":"IF","define":"DEFINE","sqrt":"SQRT","pow":"POW","fac":"FAC","list":"LIST","first":"FIRST","second":"SECOND","THIRD":"THIRD","destruct":"DESTRUCT","search":"SEARCH","mod":"MOD"}
    
tokens = ["make","set","string","id","lessthaneq","greaterthaneq","integer","greaterthan","plus","minus","times","divide","lessthan","opening","closing","left","right"]+list(keywords.values())

t_ignore =  "  \t"

def t_colon(t):
    r'\;'
    t.type =  keywords.get(t.value,"colon")
    return t 

def t_sets(t):
	 'r[a-zA-Z_][a-zA-Z_0-9]*'
	 t.type = keywords.get(t.value,"set")
	 return t 
     

def t_print(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"print")
    return t 
	
def t_exist(t):
   'r[a-zA-Z_][a-zA-Z_0-9]*'
   t.type  = keywords.get(t.value,"exist")
   return t 


def t_div_m(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"mod")
    return t

def t_maps(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"map")
    return t

def t_cons(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type =  keywords.get(t.value,"cons")
    return t 


def t_intersection(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"intersection")
    return t 


def t_union(t):
   'r[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = keywords.get(t.value,"union")
   return t 

def t_first(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"first")
    return t 

def t_second(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"second")
    return t 

def t_third(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"third")
    return t 


def t_fourth(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"fourth")
    return t 

def t_fifth(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"fifth")
    return t 

def t_sixth(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"sixth")
    return t


def t_seventh(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"seventh")
    return t

def t_eighth(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"eighth")
    return t

def t_nineth(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"nineth")
    return t   

def t_tenth(t):
    'r[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"tenth")
    return t 

def t_identiifer(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type =  keywords.get(t.value,"id")
        return t

def t_list(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,"list")
    return t 
    
def t_times(t):
        r'\*'
        t.type =  keywords.get(t.value,"times")
        return t 
    
def t_if(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type =  keywords.get(t.value,"if")
        return t 


def t_sqrt(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type  = keywords.get(t.value,"sqrt")
        return t 
    
def t_define(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'        
        t.type  = keywords.get(t.value,"define")
        return t
    
def t_plus(t):
        r'\+'
        t.type =  keywords.get(t.value,"plus")
        return t
 

    
def t_error(t):
        t.lexer.skip(1)




def t_string(t):
		'r("[^"]*")|(\'[^\']*\')'
		t.type = keywords.get(t.value, "string")
		return t


def t_integer(t):
         r'\d+'
         t.type  = keywords.get(int(t.value),"integer")
         return t


def t_minus(t):
        r'\-'
        t.type =  keywords.get(t.value,"minus")
        return t


def t_divide(t):
        r'\\'
        t.type  = keywords.get(t.value,"divide")
        return t
    


def t_greaterthan(t):
        r'\>'
        t.type =  keywords.get(t.value,"greaterthan")
        return t


def t_lessthan(t):
        r'\<'
        t.type = keywords.get(t.value,"lessthan")
        return t
    

    
def t_opening(t):
        r'\('
        t.type =  keywords.get(t.value,"opening")
        return t


def t_closing(t):
        r'\)'
        t.type  = keywords.get(t.value,"closing")
        return t





def t_fac(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type  = keywords.get(t.value,"fac")
        return t



def t_greaterthaneq(t):
        'r>='
        t.type  = keywords.get(t.value,"greaterthaneq")
        return t


def t_sin(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = keywords.get(t.value,"sin")
        return t


def t_cos(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type  = keywords.get(t.value,"cos")
        return t


def t_lessthaneq(t):
        'r<='
        t.type = keywords.get(t.value,"lessthaneq")
        return t




def t_pow(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = keywords.get(t.value,"pow")
        return t


    

scanner = scanner.lex()


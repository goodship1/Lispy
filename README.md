# Lispy

An small Lisp like  Language 


# REPL IT
Using the following command python3 Repl.py demo below.

https://user-images.githubusercontent.com/10147276/201181288-030e0f49-7439-4678-8bfe-0438bf8d000d.mp4



# Operations 

```python 
#Binary Operations

(+ 1 1)#add
(- 1 10)#minus
(* 1 1)# times

#Compare Operations

(< 20 100)#Lessthan 
(> 1 0)#Greaterthan 
(<= 20 1)#Lessthanequal
(>= 2 1)# Greaterthanequal

# Define Variables 
(define x + 1 1)

(define c * 20 1)
(define y <  1 100)
(define name  'lipsy')

(define top  if > 2  1  + 1 2  * 1  3)
(fac 10)# factorial 

# lists 

(define new_list cons  ( 1 2 3 1) ( 2 3 1 3 ))
(define str_list list 'a' 'b')

(list 1) # [1]
(list  1 23 1 .. n)# list of n elements
(define x list  1 2 3 1)# defining  a list variable
(first x) # returns the first element of x's list 
(cons ( 1 3 1 ) ( 2  1 3))# appends two lists together
(define y list 2 1 3 1 )
(cons x y) # appends x onto y
(define c first list 1 2 3 1) #c= 1

# List Operations 
# map + * / -
(map + list ( 1 2 3 1) list ( 2 3 1 1))
(define map + list ( 1 2 3 1) list(2 3 1 1))

(search (args) list)

# Functions 
(defunc add_two (x) (+ 2 x )) 
(add_two(3))

# Trig Operations

(cos 2) # cos function
(sin 200) sin function

# If Then  Else Statements

(if > 1 0 + 2 1  * 6 1)
(if > x y + x y * x y)

```

# Interacting with Interperter

Create an .ls file similar to demo.ls file  and run the following command python3 Lipsy.py file.ls



https://user-images.githubusercontent.com/10147276/201185253-a8f4b786-5c6c-4792-9459-29a107461a56.mp4

# Todo
- Error handling of keywords.
- Function Improvement.
- Pattern matching.



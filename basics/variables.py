x  = 5
y = 4

print(x)
print(y)

a = "alice"
print(a)

"""
Variable are containers for storing data values 


A name variable can not start with a number 
A viarable name can only conatain alpha-numeric characters and underscores(A-z,0-9,and_)


ILLEGLE VARIABLES

2myvar = "Alex"
my-var = "Daniel"
my var = "Bob"

Variable names are case-sensitive

"""

"This is a One value to multiple variables"

a = b = c = "Pizza"

print(a)
print(b)
print(c)

"Globle Variables"
"If you ues gloable keyword , Varible belong to globle scope."

def Globle():
    global D 
    D = "I like Pizza"


Globle()

print(D)
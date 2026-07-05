"""Operators are used to perform operation on variables and values

Arithmetic Operators

"""
x = 15
y = 4 

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

""" Assignment Operators """


x = 5 
print(x)

x+=3
print(x)

x-=3
print(x)

x*=3
print(x)

x/=3
print(x)

x%=3
print(x)

x//=3
print(x)

x**=3
print(x)

x =int(x)
x |= 3
print(x)

x ^= 3
print(x)

x >>= 3
print(x)

x <<= 3
print(x)

print(x:=3)


""" 

Ternary Operators 
allows you to assign one value if a condition is true , and another if it is false

"""

num = 6

y = "WEEKEND!" if num > 5 else "Workday"
print(y)

""" 
Comparison Operators
return True or False based on the comparison

"""

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	                      Example	
---------------------------------------------------------------------
and 	Returns True if both 	              x < 5 and  x < 10	
        statements are true
---------------------------------------------------------------------
or	    Returns True if one of the	          x < 5 or x < 4	
        statements is true
---------------------------------------------------------------------
not	    Reverse the result,returns  	      not(x < 5 and x < 10)
        False if the result is true

"""

x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
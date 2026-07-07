"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

"""

a = 33
b = 200 
if a > b:
    print("a is greater than b")
else:
    print("b is greater that a")


age = 18 
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")
else:
    pass


"""
The Elif Keyword

The elif keyword is Python's way of saying "if the previous conditions were not true,
then try this condition".

The elif keyword allows you to check multiple expressions for True and 
execute a block of code as soon as one of the conditions evaluates to True.

"""

a = 33 
b = 33 
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")


score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


"""
The Else Keyword

The else keyword catches 
anything which isn't caught by the preceding conditions.

The else statement is executed when the 
if condition (and any elif conditions) evaluate to False.

"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


"""
Short Hand If
If you have only one statement to execute,
you can put it on the same line as the if statement.

"""

a = 5 
b = 2
if a > b : print("a is greater that b")

a = 2
b = 330
print("A") if a > b else print("B")

"""
Python Logical Operators
Logical operators are used to combine conditional statements. Python has three logical operators:

and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true

"""

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the movie!")
else:
    print("You cannot enter.")


is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")
else:
    print("Time to work!")

is_raining = False

if not is_raining:
    print("Let's go play outside!")
else:
    print("Stay inside!")



score = 85
attendance = 90

if score >= 80 and attendance >= 75:
    print("You passed!")
elif score >= 60 or attendance >= 50:
    print("You need improvement")
else:
    print("You failed")
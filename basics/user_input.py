import math 

""" 
User Input
Python allows for user input.

That means we are able to ask the user for input.

The following example asks for your name,
and when you enter a name, it gets printed on the screen:

"""

print("Enter your name: ")
name = input()
print(f"Hello {name}")

"""
Using prompt
In the example above, the user had to input their name on a new line. The Python input() function has a prompt parameter,
which acts as a message you can put in front of the user input, on the same line:

"""

name = input("\nEnter your name: ")
print(f"Hello {name}")
print("\n")

"""
Multiple Inputs
You can add as many inputs as you want,
Python will stop executing at each of them, waiting for user input:

"""

name = input("Enter your name: ")
print(f"Hello {name}")

fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

"""
Input Number
The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.

You can convert the input into a number with the float() function:

"""

x = input("Enter a number: ")

y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")
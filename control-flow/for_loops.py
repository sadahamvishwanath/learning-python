"""
Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

"""

fruits = ["apple","banana","cherry"]
for _ in fruits:
    print(_)


print("\n")
for x in "Banana":
    print(x)

"""The break Statement
With the break statement 
we can stop the loop before it has looped through all the items:
"""

print("\n")
fruits =  ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


"""
The continue Statement
With the continue statement we can stop the current iteration of 
the loop, and continue with the next:

"""

print("\n")
fruits =  ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)



"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default,
and increments by 1 (by default), and ends at a specified number.

"""
print("\n")
for x in range(6):
    print(x)


print("\n")
for x in range(2,6):
    print(x)


print("\n")
for x in range(2, 30, 3):
    print(x)

"""
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed 
one time for each iteration of the "outer loop":

"""
print("\n")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
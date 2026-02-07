# For Loops -> Basics
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# The loop will iterate over each item in the fruits list and print it out.
# You can also use the range() function to loop through a set of code a specified number of times.
for i in range(5):
    print(i)
# This will print numbers from 0 to 4.
# You can specify a starting number by adding a parameter to the range() function.
for i in range(2, 6):
    print(i)
# This will print numbers from 2 to 5.
# You can also specify a step value by adding a third parameter to the range() function.
for i in range(1, 10, 2):
    print(i)
# This will print odd numbers from 1 to 9.

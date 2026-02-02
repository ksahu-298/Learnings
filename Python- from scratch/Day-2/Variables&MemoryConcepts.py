# Variable is the name that stores a value in memory
a= 10
y = "Singham"
print(a, "\n", y)

# here in the above code snippet a and y behave as a variable
#Key Points:-
#Python automatically decides the data type of variable based on the value assigned to it.
# we can check the data type of variable using type() function
print(type(a))   # Output: <class 'int'>
print(type(y))   # Output: <class 'str'>
# use id() function to check the memory address of variable
print(id(a))
print(id(y))

# use typecasting to change the data type of variable
b = str(a)  # converting integer to string
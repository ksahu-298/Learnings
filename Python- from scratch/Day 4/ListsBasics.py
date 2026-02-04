# What are lists in Python?
# Lists are used to store multiple items in a single variable.
# Lists are ordered, changeable, and allow duplicate values.
# Lists are defined by placing items inside square brackets [].
# Example of a list
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)


# length of list 
print(len(fruits))

# Accessing items in a list
print(fruits[0])  # First item
print(fruits[2])  # Third item

# Looping through a list
for item in range(len(fruits)):
    print(f'The {item} item is: {fruits[item]}')
    
# Modifying items in a list
fruits[1] = "orange"
print(fruits)
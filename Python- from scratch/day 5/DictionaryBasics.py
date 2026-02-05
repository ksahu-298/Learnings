# What is Dictionary in python -> A dictionary is a built-in data type in Python that allows you to store and manage data in key-value pairs.
# Each key in a dictionary is unique and is used to access its corresponding value. But if we try to add two keys with the same name, the latter will overwrite the former.
# Dictionaries are mutable, meaning you can change their content (add, remove, or modify key-value pairs) after they are created.
# Dictionaries are defined using curly braces {} with key-value pairs separated by commas.
# using the get() method to access a key that does not exist will return None instead of raising an error.
# Creating a dictionary
student = {
    "name": "Karan",
    "age": 21,
    "courses": ["Math", "CompSci"],
    "city": "Kanpur"
}

print(student)

# Accessing values in a dictionary
print(student["name"])  # Output: Karan
print(student.get("age"))  # Output: 21
print(student["courses"])
print(student["courses"][0])  # Output: Math
print(student.get("city"))  # Output: Kanpur

# Adding key-value pairs to a dictionary
student["email"] = "karansahu.engineer@gmail.com"
print(student)
    
# Modifying values in a dictionary
student["age"] = 22
print(student)

# Removing key-value pairs from a dictionary
student.pop("city") # removes the key 'city' and its value
print(student)
del student["courses"]  # removes the key 'courses' and its value
print(student)
# Using the popitem() method to remove the last inserted key-value pair
last_item = student.popitem()
print("Removed item:", last_item)
print(student)
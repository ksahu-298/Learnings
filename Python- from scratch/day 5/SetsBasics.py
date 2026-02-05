# Sets -> Unordered collection of unique items
# Creating a set
languages = {"Python", "Java", "C++", "JavaScript", "Python"}  # Duplicate "Python" will be ignored
print("Initial set:", languages)

# create an empty set
emptySet = set()
print(type(emptySet))  # Output: <class 'set'>

# adding and removing elements 
languages.add("Ruby")
print("After adding Ruby:", languages)
languages.remove("Java")  # Raises KeyError if not found
print("After removing Java:", languages)
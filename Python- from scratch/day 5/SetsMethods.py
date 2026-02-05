# Some basics and important methods of sets in Python
# Sets -> Unordered collection of unique items
# add() method -> Adds an element to the set
fruits = {"apple", "banana", "cherry"}
print("Initial set of fruits:", fruits)
fruits.add("orange")
print("After adding orange:", fruits)

# update() method -> Adds multiple elements to the set
fruits.update(["mango", "grape"])
print("After updating with mango and grape:", fruits)

# remove() method -> Removes a specified element from the set
fruits.remove("banana")  # Raises KeyError if not found
print("After removing banana:", fruits)

# discard() method -> Removes a specified element from the set if it is present
fruits.discard("kiwi")  # Does not raise an error if not found
print("After discarding kiwi (not present):", fruits)

# pop() method -> Removes and returns an arbitrary element from the set
removed_fruit = fruits.pop()
print("After popping an element:", fruits)
print("Popped fruit:", removed_fruit)

# clear() method -> Removes all elements from the set
fruits.clear()
print("After clearing the set:", fruits)

# union() method -> Returns a new set with elements from both sets
setA = {1, 2, 3}
setB = {3, 4, 5}
setC = setA.union(setB)
print("Union of setA and setB:", setC)

# intersection() method -> Returns a new set with elements common to both sets
numberSet = {2,3,2,4,5,6}
commonNumbers = setA.intersection(numberSet)
print("Intersection of setA and numberSet:", commonNumbers)

# difference() method -> Returns a new set with elements in the first set but not in the second
diffSet = setA.difference(numberSet)
print("Difference of setA and numberSet:", diffSet)

# symmetric_difference() method -> Returns a new set with elements in either set but not in both
symDiffSet = setA.symmetric_difference(numberSet)
print("Symmetric difference of setA and numberSet:", symDiffSet)

# isdisjoint() method -> Returns True if two sets have no elements in common
setX = {7, 8}
setY = {9, 10}
print("Are setX and setY disjoint?", setX.isdisjoint(setY))

# issubset() method -> Returns True if all elements of the set are in another set
subsetCheck = {1, 2}.issubset(setA)
print("Is {1, 2} a subset of setA?", subsetCheck)

# issuperset() method -> Returns True if the set contains all elements of another set
supersetCheck = setA.issuperset({2, 3})
print("Is setA a superset of {2, 3}?", supersetCheck)

# copy() method -> Returns a shallow copy of the set
originalSet = {10, 20, 30}
copiedSet = originalSet.copy()
print("Original set:", originalSet)
print("Copied set:", copiedSet)

# frozenset -> Immutable version of a set
immutableSet = frozenset([1, 2, 3, 4])
print("Immutable frozenset:", immutableSet)
# Trying to add an element to frozenset will raise an AttributeError
# immutableSet.add(5)  # Uncommenting this line will raise an error
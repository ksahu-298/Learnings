# Tuples - > Immutable Sequences
# Tuples are similar to lists, but they cannot be changed (immutable) after creation.
# They are defined using parentheses () instead of square brackets [].
# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print("Original Tuple:", my_tuple)

# Accessing elements in a tuple
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

# Slicing a tuple
print("Sliced Tuple (1:4):", my_tuple[1:4])

# Tuples are immutable, so the following line would raise an error if uncommented
# my_tuple[0] = 10  # This will raise a TypeError
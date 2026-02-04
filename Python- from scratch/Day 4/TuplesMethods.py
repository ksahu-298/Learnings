# There are various methods that can be used with tuples in Python. Here are some common ones:  
# 1. count(): This method returns the number of times a specified value appears in the tuple.
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_twos = my_tuple.count(2)
print("Count of 2 in tuple:", count_of_twos)

# 2. index(): This method returns the index of the first occurrence of a specified value in the tuple.
index_of_three = my_tuple.index(3)
print("Index of 3 in tuple:", index_of_three)
# Note: Tuples are immutable, so they do not have methods that modify the tuple, such as append() or remove().

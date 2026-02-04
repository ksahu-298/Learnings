# There are multiple methods that are being used in Lists -
#. Indexing
a= [1,2,3,4,5,6,7,8,9]
print(a.index(5))  # Output: 4 (index of first occurrence of 5)

#. Append
a.append(10)
print(a)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#. Insert
a.insert(0, 0)
print(a)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#. Remove
a.remove(5)
print(a)  # Output: [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]

#. Pop
popped_item = a.pop()
print(popped_item)  # Output: 10
print(a)  # Output: [0, 1, 2, 3, 4, 6, 7, 8, 9]

#. Clear
a.clear()
print(a)  # Output: []

#. Copy
b = [1, 2, 3]
c = b.copy()
print(c)  # Output: [1, 2, 3]


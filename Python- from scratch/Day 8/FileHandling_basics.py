# File Handling Basics in Python-
# This script demonstrates basic file handling operations in Python including creating, writing, reading, and appending to files.
# It also covers different file modes and error handling during file operations.


#Opening a file in write mode
# f = open("sample_textfile.txt", "r") # giving error 
file = open("c:\\Users\\sahuk\\OneDrive\\Desktop\\Complete Python from Scratch\\chapter 8\\sample_textfile.txt")

print("File opened successfully.")
data = file.read()
print("File content:")
print(data)
file.close()
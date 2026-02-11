# by using with keyword

# reading the entire file content
with open("C:\\Users\\sahuk\\OneDrive\\Desktop\\Complete Python from Scratch\\chapter 8\\sample_textfile.txt", "r") as file:
    print(file.read())
# The file is automatically closed after the with block

print("\n File reading completed. \n")

# reading file line by line means reading only one line
with open("C:\\Users\\sahuk\\OneDrive\\Desktop\\Complete Python from Scratch\\chapter 8\\sample_textfile.txt", "r") as file:
    line_1 = file.readline()
    print("line 1: ", line_1)
    line_2 = file.readline()
    print("line 2: ", line_2)
    line_3 = file.readline()
    print("line 3: ", line_3)
    line_4 = file.readline()                                     # our file has only 3 lines so this will return empty string
    print("line 4: ", line_4)
# The file is automatically closed after the with block

print("\n File reading completed. \n")

# reading all lines into a list
with open("C:\\Users\\sahuk\\OneDrive\\Desktop\\Complete Python from Scratch\\chapter 8\\sample_textfile.txt", "r") as file:
    lines = file.readlines()
    print(lines)

print("\n File reading completed. \n")
# The file is automatically closed after the with block

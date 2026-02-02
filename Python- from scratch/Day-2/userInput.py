name = input("Enter your name: ")
print("Hello, " + name + "!") # or print("Hello", name)

# input() always returns string, Convert it before performing calculations

age = int(input(name + ", Enter your age: "))  # converting input to integer
print(name , "you will be", age + 1, "years old next year.")

love = input("do you love someone : ")
print(name , "loves ❤️ ", love)
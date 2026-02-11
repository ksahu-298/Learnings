with open("C:\\Users\\sahuk\\OneDrive\\Desktop\\Complete Python from Scratch\\chapter 8\\Practice 3\\notes.txt", "w") as file:
    file.write(""" Core Fundamentals :- \n1.) Variables, dynamic typing, type casting \n2.) Input/output handling \n3.) Operators \n4.) Control flow (if-else, loops) \n5.) Functions and modular programming \n6.) Data structures (lists, tuples, dictionaries, sets) \n7.) Error handling (try-except) \n8.) File handling basics \n\n Object-Oriented Programming (OOP) :- \n1.) Classes and objects \n2.) Inheritance \n3.) Polymorphism \n4.) Encapsulation \n5.) Abstraction \n6.) Special methods (dunder methods) \n\n Advanced Topics :- \n1.) List comprehensions and generator expressions \n2.) Decorators and higher-order functions \n3.) Lambda functions \n4.) Modules and packages \n5.) Working with libraries (e.g., NumPy, Pandas) \n6.) Introduction to web frameworks (e.g., Flask, Django) \n\n Best Practices :- \n1.) Code readability and commenting \n2.) 
Version control with Git \n3.) Testing and debugging \n4.) Performance optimization \n5.) Documentation \n""")
    
print("Notes file created and content written successfully.")


with open("C:\\Users\\sahuk\\OneDrive\\Desktop\\Complete Python from Scratch\\chapter 8\\Practice 3\\notes.txt", "r") as file:
    lines = file.readlines()
    count = 0
    for line in lines:
        count += 1
    print(f"Total number of lines in the notes file: {count}")
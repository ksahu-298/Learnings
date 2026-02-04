# Conditional Statements in Python --> These are used to perform different actions based on different conditions.
# Example of if, elif, and else statements
age = 18
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
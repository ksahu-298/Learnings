# Write a program to check grade based on marks (A/B/C/D) using if-elif and else

marks = int(input("Enter your marks :  "))

if marks>=90:
    print("Grade A")

elif 90>marks>=80:
    print("Grade B")

elif 80>marks>=70:
    print("Grade C")

elif 70>marks>=60:
    print("Grade D")

else:
    print("Grade F")
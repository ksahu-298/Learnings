# Create a dictionary named marks to store marks of 3 subjects.
# Add the subjects one by one and print the final dictionary

maths_mark = int(input("Enter Maths mark: "))
science_mark = int(input("Enter Science mark: "))
computer_mark = int(input("Enter Computer mark: "))

marks = {
    "Maths": maths_mark,
    "Science": science_mark,
    "Computer": computer_mark
}

print(f"The marks of {marks.keys()} are {marks.values()} respectively.")

# OR
marks_2 = {}
marks_2["Maths"] = maths_mark
marks_2["Science"] = science_mark
marks_2["Computer"] = computer_mark
print(marks_2)


# write a program to check whether a number is positive, negative or zero.
number = int(input("Enter any integer : "))
if number < 0:
    print(f'Your number {number} is negative')
elif number == 0:
    print(f'Your number {number} is zero')
else:
    print(f'Your number {number} is positive')
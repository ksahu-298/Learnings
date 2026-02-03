# Take 2 number as an input from user and return the sum, difference, multiplication and division of those numbers 
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
print(f'Addition: {num1 + num2}')
print(f'Subtraction: {num1 - num2}')
print(f'Multiplication: {num1 * num2}') 
print(f'Division : {num1 / num2}')

# Take 2 numbers as input from user and check whether 1st number is greater than 2nd number or not
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is not greater than {b}")

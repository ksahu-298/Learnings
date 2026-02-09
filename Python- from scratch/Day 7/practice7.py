#Write a function square(num) that returns the square of a number.
def square_num(num):
    return(num*num)

number = int(input("Enter the number you want to square: "))
square = square_num(number)
print(f"The square of the number {number} is : {square}")


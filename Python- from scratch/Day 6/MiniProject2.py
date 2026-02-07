# Mini Project – Multiplication Table
num = int(input("Enter a number whose table you want to print: "))
end= int(input("Enter the ending number for the table: "))
print(f"\nMultiplication table of {num} upto {end} is:\n")
for i in range(1, end+1):
    print(f"{num} x {i} = {num*i}")
# Print the multiplication table of a given number up to a specified range using for loop and range().
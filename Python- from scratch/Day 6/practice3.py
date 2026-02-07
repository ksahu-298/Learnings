# Program Write a program to print all even numbers between 1 and 50 using a while loop.(Hint: Use the modulus operator % to check for even numbers.)Example Output: 2 4 6 8 ... 50

a= 1
while a<=51:
    if a%2== 0:
        print(f'{a} is even')
    a+=1
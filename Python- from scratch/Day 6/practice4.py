#Write a program that prints the sum of first n natural numbers.For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.(Hint: Keep a running total inside the loop.)
sum = 0
n = int(input("Enter a natural number: "))
count = 1
while count <= n:
    sum += count
    count += 1
    print(f"The sum of first {count-1} natural numbers is {sum}")
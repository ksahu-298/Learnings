# Mini Project – Guess the Number Game
import random
num = random.randint(1, 100)
print(num)
guess = None
while guess != num:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")
#random number
import random

x = random.randint(1, 100)

while True:
    guess = int(input("Guess number (1-100) or 0 to exit: "))

    if guess == 0:
        print(f"You surrendered! The number was {x}")
        break
    elif guess == x:
        print("Correct! You win.")
        break
    elif guess > x:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
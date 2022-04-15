# Write a program to guess a number between 1 to 9.

import random

number = random.randint(1, 10)
guess_number = int(input("Enter your guess number: "))
counter = 0

while guess_number > 0:
    guess_number -= 1
    counter += 1
    your_guess = int(input("What is your guess: "))
    
    if your_guess == number:
        print(f"Congrats, your guess is True and got it on the {counter} times.")
        break
    elif your_guess > number:
        print("You should decrease your guess.")
    else:
        print("You should increase your guess.")
        
    if guess_number == 0:
        print("Unfortunately, you failed.", f"The number was {number}.")


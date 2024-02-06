"""Number Guessing Game"""
from random import randint

SECRET : int = randint(1,5)
correct: bool = False

while not correct: #correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct!",(guess),"is the number!")
        # something to help us exit
        correct = True
    else:
        print("Guess again")
    if guess > randint(1,5): 
        print("Error", (guess), "too high!")
    if guess <  randint(1,5):
        print("Error", (guess), "too low!")
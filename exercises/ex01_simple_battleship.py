"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730410860"
my_ship: str = input("Pick a secret boat location between 1 and 4: ")
other_ship: str = input("Guess a number between 1 and 4:")
user_number: int = int(my_ship)
other_number: int = int(other_ship)
emojiB: str = "\U0001F7E6"
emojiR: str = "\U0001F7E5"
emojiW: str = "\U00002B1C" 


# if user_number is less than 1 print "Error! too low!"
if user_number < 1: 
  print("Error!", str(user_number), "too low!")
if user_number > 4:
  print("Error!", str(user_number), "too high!")
 # if other_number is less than user_number
if other_number < user_number: 
  print("Error!", str(other_number), "too low!")
if other_number > user_number:  
  print("Error!", str(other_number), "too high!")
if other_number == user_number:
  print ( emojiB + (emojiR)+ emojiB*2 )
else: 
  print ( emojiB*2 + emojiW + emojiB )
if other_number == user_number: 
  print("Correct! You hit the ship.")
else: 
  print("Incorrect! You missed the ship.")



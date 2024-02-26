"""One Shot Battleship."""
__author__ = "730410860"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2 
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C" 


guess_row: int = int(input("Guess a row: "))
while guess_row < 1 or guess_row > grid_size:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

guess_column: int = int(input("Guess a column:"))
while guess_column < 1 or guess_column > grid_size: 
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

result_box: str = " "
if (guess_row == secret_row) and (guess_column == secret_column):
    result_box = (RED_BOX)
else: 
    result_box = (WHITE_BOX)

row_counter: int = 1
while row_counter <= grid_size:
    emoji_row: str = " "
    column_counter: int = 1
    if guess_row == row_counter:
        while column_counter <= grid_size:
            if guess_column == column_counter:
                emoji_row += result_box
            else: 
                emoji_row += BLUE_BOX
            column_counter = column_counter + 1
    else: 
        while column_counter <= grid_size:
            emoji_row += BLUE_BOX
            column_counter = column_counter + 1
    print(emoji_row)
    row_counter = row_counter + 1

if (guess_column) == (secret_column) and (guess_row) == (secret_row):
    print("Hit!")
elif (guess_row == secret_row): 
    print("Close! Correct row, wrong column.")
elif (guess_column == secret_column):
    print("Close! Correct column, wrong row.")
else: 
    print("Miss!")





   
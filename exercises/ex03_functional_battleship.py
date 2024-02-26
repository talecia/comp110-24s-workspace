"""Functional Battleship."""
__author__ = "730410860"
from random import randint

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C" 

# Part 1 
def input_guess(grid_size: int, row_guess: str) -> int:
    assert row_guess == "row" or row_guess == "column"
    new_variable: int = 0
    if row_guess == "row":
        new_variable = int(input("Guess a row: "))
        
    if row_guess == "column":
        new_variable = int(input("Guess a column: "))
    while new_variable > grid_size or new_variable <= 0:
        new_variable = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: ")) 
    return new_variable

# Part 2 
def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guess: bool) -> None: 
    result_box: str = " "
    if (correct_guess == True) :
        result_box = (RED_BOX)
    else:
        result_box = (WHITE_BOX)


    row_counter: int = 1
    while row_counter <= grid_size:
        emoji_row: str = ""
        column_counter: int = 1
        if row_guess == row_counter:
            while column_counter <= grid_size:
                if column_guess == column_counter:
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

# Part 3
def correct_guess(secret_row: int, secret_column: int,row_guess: int , column_guess: int,) -> bool: 
    return (row_guess) == (secret_row) and (column_guess) == (secret_column)

# Part 4
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    current_turn: int = 1
    max_turn: int = 5
    won: bool = False
    while current_turn <= max_turn and not won:
        print(f"=== Turn {current_turn}/{max_turn} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        correct: bool  = correct_guess(secret_column, secret_row, column_guess,row_guess)
        print_grid(grid_size, row_guess, column_guess, correct)
        if correct:    
            print("Hit!")
            print(f"You won in {current_turn}/ 5 turns!")
            won = True
        else: 
            print("Miss!")
            if current_turn == 5:
                print(f"{current_turn}/5 - Better luck next time!")
            current_turn += 1 
if __name__ == "__main__":
    grid_size: int = randint(3,5)
    main(grid_size, randint(1, grid_size), randint(1, grid_size))


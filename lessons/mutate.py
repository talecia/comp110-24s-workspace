"""Mutating functions."""
__author__ = "730410860"

# manual_append
def manual_append(parameter1: list[int], parameter2: int) -> None: 
    parameter1.append(parameter2)

# double()
def double(parameter1: list[int])-> None:
    counter: int = 0 
    while counter < len(parameter1):
        (parameter1[counter]) *= 2
        counter += 1
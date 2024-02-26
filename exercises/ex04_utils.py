"""Utils Assignment."""
__author__ = "730410860"

# Part 1
def all(number1: list[int], number2: int) -> bool:
    if not number1:
        return False
    for count in number1:
        if count != number2:
            return False
    return True
# Part 2
def max(big1: list[int]) -> int:
    if len(big1) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = big1[0]
    for digit in big1[1:]:
        if digit > maximum:
            maximum = digit
    return maximum
# Part 3 
def is_equal(real1: int, real2: int) -> bool:
    if len(real1) != len(real2):
        return False
    for fake in range(len(real1)):
        if real1[fake] != real2[fake]:
            return False
    return True
# Part 4
def extend(long1: list[int], long2: list[int]) -> None:
    long1.append(long2)

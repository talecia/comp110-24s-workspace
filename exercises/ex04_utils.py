"""Utils Assignment."""
__author__ = "730410860"


def all(number1: list[int], number2: int) -> bool:
    """Determine if int retuns a bool."""
    if not number1:
        return False
    for count in number1:
        if count != number2:
            return False
    return True


def max(big1: list[int]) -> int:
    """Returning largest value given."""
    if len(big1) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = big1[0]
    for digit in big1[1:]:
        if digit > maximum:
            maximum = digit
    return maximum


def is_equal(real1: list[int], real2: list[int]) -> bool:
    """Checking if lengths match."""
    if len(real1) != len(real2):
        return False
    for fake in range(len(real1)):
        if real1[fake] != real2[fake]:
            return False
    return True


def extend(long1: list[int], long2: list[int]) -> None:
    """Appends the second list's values to the end."""
    counter: int = 0
    while len(long2)  > counter:
        long1.append(long2[counter])
        counter += 1

    
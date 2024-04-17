"""Writing a Recursive Function."""
__author__ = "730410860"


def f(n: int, k: int) -> int:
    """If else statement presents base case and recursive rule."""
    if n == 0: 
        return 0
    else:
        return k + f(n-1, k)

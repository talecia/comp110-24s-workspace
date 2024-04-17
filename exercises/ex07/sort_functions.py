"""Functions that implement sorting algorithms."""

__author__ = "730410860"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    sort_idx: int = 0
    for unsort_idx in range(1,len(x)):
        current = x[unsort_idx]
        while unsort_idx > 0 and current < x[unsort_idx - 1]:
            x[unsort_idx], x[unsort_idx - 1] = x[unsort_idx - 1],x[unsort_idx]
            unsort_idx -= 1
    sort_idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    counter: int = 0
    number: int = len(x)
    for i in range(number):
        min_idx = i
        for judge in range(i + 1, number):
            if x[judge] < x[min_idx]:
                min_idx = judge
        if min_idx != 1:
            x[min_idx], x[i] = x[i], x[min_idx]
    return None
    
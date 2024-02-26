"""Summing the elements of a list using different loops."""
__author__ = "730410860"
def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum_val: float = 0.0
    while index < len(vals):
        sum_val += vals[index]
        index += 1
    return sum_val
def f_sum(vals: list[float]) -> float:
    sum_val: float = 0.0
    for val in vals:
        sum_val += val
    return sum_val
def f_range_sum(vals: list[float]) -> float:
    sum_val: float = 0.0
    for idx in range(len(vals)):
        sum_val += vals[idx]
    return sum_val
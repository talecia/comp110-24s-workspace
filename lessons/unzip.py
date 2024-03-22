"""Splitting a dictionary into two lists. """
__author__ = "730410860"

def get_keys(dict_input: dict[str, int]) -> list[str]:
    """Function Producing list of keys in input dictionary."""
    key_variable: list[str] = list( )
    for keys in dict_input:
        key_variable.append(keys)
    return key_variable

def get_values(dict_input: dict[str, int]) -> list[int]:
    """Function Producing list of vlaues in input dictionary."""
    value_variable: list[int] = list( )
    for values in dict_input:
        value_variable.append(dict_input[values])
    return value_variable


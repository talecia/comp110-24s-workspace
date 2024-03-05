"""DIctionary Practice with different variables."""
__author__ = "730410860"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """Keys of input list become value of output list."""
    invert_variable: list[str] = { }
    for keys, value in dict_input.items():
        if value in invert_variable:
            raise KeyError("Theres is a duplicate value.")
        invert_variable[value] = keys
    return invert_variable


def favorite_color(dict_input: dict[str, str]) -> str:
    """Returning a list of the most popular colors."""
    color_variable: list[str] = { }
    for colors in dict_input:
       color_variable[colors] = color_variable + 1
    popular_color = None
    big_count: int = 0
    for colors, count in color_variable:
        if count > big_count or (count == big_count and colors < popular_color):
            popular_color = colors
            big_count = count
    return popular_color


def count(number1: list[str]) -> dict[str,int]: 
    """Key values in given list will be in the input list."""
    numbers: list[str] = { }
    for num in number1:
        if num in numbers:
            numbers[num] += 1
        else:
             numbers[num] = 1
    return numbers


def alphabetizer(letter: list[str]) -> dict[str, list[str]]:
    """Unique list of words will be returned in an alphabetized list."""
    dict_alphabet: dict[str, list[str]] = {}
    for word in letter:
        top_letter = word[0].lower()
        if 'a' <= top_letter <= 'z':
            if top_letter not in dict_alphabet:
                dict_alphabet[top_letter] = []
            dict_alphabet[top_letter].append(word)
    return dict_alphabet


def update_attendance(dict_attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance with new added information"""
    if day in dict_attendance:
        dict_attendance[day].append(student)
    else:
        dict_attendance[day] = [student]
        
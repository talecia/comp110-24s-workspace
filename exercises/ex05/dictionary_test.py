"""Dictionary Unit Test Practice with different variables."""
__author__ = "730410860"

from exercises.ex05.dictionary import invert, count, favorite_color, alphabetizer, update_attendance


def test_invert_use1() -> None:
    """Test basice use case for invert function."""
    i: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    invert(i)
    ret_val: list[str] = {'x': 'c', 'y': 'b', 'z': 'a'}
    assert invert(i) == ret_val


def test_invert_use2() -> None:
    """Test basic use case for invert function."""
    i: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    invert_dict: dict[str, str] = invert(i)
    ret_val: list[str] = {'x': 'c', 'y': 'b', 'z': 'a'}
    assert invert_dict == ret_val


def test_invert_edge() -> None:
    """Test basic edge case for invert function."""
    empty_invert: dict[str, str] = {}
    invert_dict: dict[str, str] = invert(empty_invert)
    assert invert_dict == empty_invert


def test_count_use1() -> None:
    """Test basic use case for count function."""
    n: list[str] = ["5", "3", "1"]
    count(n)
    ret_val: dict[str, list[str]] = {'5': 1, '3': 1, '1': 1}
    assert count(n) == ret_val


def test_count_use2() -> None:
    """Test basic use case for count function."""
    n: list[str] = ["a", "b", "c", "a", "b", "a"]
    count(n)
    ret_val: dict[str, list[str]] = {'a': 3, 'b': 2, 'c': 1}
    assert count(n) == ret_val


def test_count_edge() -> None:
    """Test basic edge case for count function."""
    empty_count: list[str] = []
    count(empty_count)
    count_dict: dict[str, list[str]] = {}
    assert count(empty_count) == count_dict


def test_favorite_color_use1() -> None: 
    """Test basic use case for favorite_color function."""
    c: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    ret_val: str = "blue"
    assert favorite_color(c) == ret_val


def test_favorite_color_use2() -> None:
    """Test basic use case for favorite_color function."""
    c: dict[str, str] = {"Jordan": "green", "Josh": "red", "Enrique": "green"}
    favorite_color(c)
    ret_val: str = "green"
    assert favorite_color(c) == "green"
    assert favorite_color(c) == ret_val


def test_favorite_color_edge() -> None: 
    """Test basic edge case for favorite_color function."""
    blank_color: dict[str, int] = {}
    favorite_color(blank_color)
    my_color = None
    assert favorite_color(blank_color) == my_color


def test_alphabetizer_use1() -> None:
    """Test baisc use case for alphabetizer function."""
    alpha: dict[str, list[str]] = {"apple", "banana", "orange", "kiwi", "grape", "lemon", "pear"}
    alphabetizer(alpha)
    ret_val: dict[str, list[str]] = {'a': ['apple'], 'b': ['banana'], 'g': ['grape'], 'k': ['kiwi'], 'l': ['lemon'], 'o': ['orange'], 'p': ['pear']}
    assert alphabetizer(alpha) == ret_val


def test_alphabetizer_use2() -> None: 
    """Test basic use case for alphabetizer function."""
    letters: dict[str, list[str]] = {"$Apple", "#Banana", "Carrot"}
    ret_val: dict[str, list[str]] = {'c': ["Carrot"]}
    assert alphabetizer(letters) == ret_val


def test_alphabetizer_edge() -> None:
    """Test basic edge case for alphabetizer function."""
    clear_letters: dict[str, list[str]] = {}
    ret_val: dict[str, list[str]] = {}
    assert alphabetizer(clear_letters) == ret_val


def test_update_attendance_use1() -> None:
    """Test basic use case for update_attendance function."""
    log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    new_log: str = "Friday"
    student: str = "Melissa"
    update_attendance(log, new_log, student)
    ret_val: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Friday": ["Melissa"]}
    assert log == ret_val


def test_update_attendance_use2() -> None:
    """Test basic use case for update_attendance function."""
    log2: dict[str, list[str]] = {"Monday": ["Tati", "Kaleb"], "Tuesday": ["Cole"], "Friday": ["Melissa"]}
    new: str = "Monday"
    stud: str = "Rebecca"
    update_attendance(log2, new, stud)
    ret_val: dict[str, list[str]] = {"Monday": ["Tati", "Kaleb", "Rebecca"], "Tuesday": ["Cole"], "Friday": ["Melissa"]}
    assert log2 == ret_val


def test_update_attendance_edge() -> None: 
    """Test basic edge case for update_attendance function."""
    here: dict[str, list[str]] = {"Monday": ["Erica", "Kayla", "Rebecca"], "Tuesday": ["George"], "Friday": ["Melissa"]}
    new_day: str = "Friday"
    name: str = "Mary"
    update_attendance(here, new_day, name)
    ret_val: dict[str, list[str]] = {"Monday": ["Erica", "Kayla", "Rebecca"], "Tuesday": ["George"], "Friday": ["Melissa", "Mary"]}
    assert here == ret_val
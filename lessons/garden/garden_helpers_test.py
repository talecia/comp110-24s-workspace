"""Test my garden functions."""
__author__ = "730410860"

from lessons.garden import garden_helpers

# By_kind
def test_for_plants() -> None: 
    """Use case to test add_by_kind function when adding new plant kind."""
    test_dict: dict[str,list[str]] = {"flower": ["tulip", "sunflower" ]}
    new_plant_kind: str = "tree"
    new_plant: str = "oak"
    garden_helpers.add_by_kind(test_dict,new_plant_kind,new_plant)
    assert ("tree" in test_dict)

def test_add_kind_plant() -> None:
    """Should return new plant and kind."""
    test_dict: dict[str,list] = {}
    new_plant_kind: str = "fruit"
    new_plant: str = "peach"
    garden_helpers.add_by_kind(test_dict, new_plant_kind, new_plant)
    assert ([new_plant_kind], [new_plant])

# Add_by_date
def test_for_plant_date() -> None:
    """Edge case to test add_by_date function. """
    test_dict: dict[str,list[str]] = {}
    month: str = "June"
    plant: str = "Tomato", "Lettuce"
    garden_helpers.add_by_date(test_dict, month, plant)
    assert {month,plant}


def test_add_new_plant_month() -> None:
    """Use cae to test add_by_date function."""
    test_dict: dict[str,list[str]] = {"June": ["Tomato", "Lettuce"]}
    month: str = "June"
    plant: str = "Beets"
    garden_helpers.add_by_date(test_dict, month, plant)
    assert ("Beets" in test_dict)

# Look_up_kind_and_date
def test_lookup_planted() -> None: 
    """Use case to test lookup_by_kind_and_date function."""
    test_dict: dict[str,list] = {"flower": ["tulip", "sunflower", "peony"]}
    plants_by_kind:  dict[str, list[str]] = {"flower": ["sunflower", "peony"]}
    month_plants: dict[str,list[str]] = {"June": ["sunflower", "peony"]}
    garden_helpers.lookup_by_kind_and_date(test_dict, plants_by_kind, month_plants)
    assert ("sunflower", "peony" in test_dict)


def test_lookup_no_planted() -> None:
    """Edge case to test lookup_by_kind_and_date function."""
    by_kind_plants: dict[str,list] = {}
    month_plants: dict[str,list[str]] = {"June": ["sunflower", "peony"]}
    garden_helpers.lookup_by_kind_and_date
    assert (by_kind_plants,month_plants)
    
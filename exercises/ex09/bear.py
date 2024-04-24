"""File to define Bear class."""
__author__ = "730410860"


class Bear:
    """Represents the Bears livingn ear the river."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Creating the bears for my river simulation."""
        self.age = 0
        self.hunger_score = 0 
        return None
    
    def one_day(self):
        """Change the age of the bear by 1 and decrease the hunger by 1."""
        self.hunger_score -= 1
        self.age += 1
        return None
    
    def eat(self, num_fish: int):
        """Update Bear hunger score to increase by num fish."""
        self.hunger_score += num_fish
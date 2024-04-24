"""File to define Fish class."""


class Fish:
    """Represents Fish living near the river."""
    
    age:int 

    def __init__(self): 
        """Creating the fish for my river simulation."""
        self.age = 0 
        return None
    
    def one_day(self): 
        """Change the age of the fish by 1."""
        self.age += 1 
        return None
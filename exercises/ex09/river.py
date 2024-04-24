"""File to define River class."""
__author__ = "730410860"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:
    """Represents all animals and their aspects around the river."""
    
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        return None

    def bears_eating(self):
        return None
    
    def check_hunger(self):
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
    
    def view_river(self):
        """Prints what amount of animals in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self): 
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Gives the life in the river of one week."""
        for R in range(7):
            self.one_river_day()
        
    def check_ages(self):
        """Remove all old Fish and Bears from the River."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Removes said amount of fish from the River."""
        amount = min(amount, len(self.fish))
        self.fish = self.fish[amount: ]

    def bears_eating(self):
        """Bears eating the fish."""
        if len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
            self.remove_fish(3)    
    
    def check_hunger(self):
        """Check if Bear is too hungry."""
        bears_left = [ ]
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bears_left.append(bear)
        self.bears = bears_left        

    def repopulate_bears(self):
        """Repopulate the River with new bears."""
        bear_pairs = len(self.bears) // 2
        for B in range(bear_pairs):
            self.bears.append(Bear())
    
    def repopulate_fish(self):
        """Repopulate the River with new fish."""
        fish_pairs = len(self.fish) // 2
        for F in range(fish_pairs):
            for p in range(4):
                self.fish.append(Fish())

"""River Simulation with all animals and a river."""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear
from exercises.ex09.river import River

my_river = River(num_fish=10, num_bears=2)

class RiverSimulation:
    def __init__(self):
        self.my_river = River(num_fish=10, num_bears=2)  
        return None
    
  


    my_river.view_river()
    my_river.one_river_week()
    my_river.check_ages()
    my_river.check_hunger
   



# Map Objects module - contains all inanimate entities to be encountered
import items
import random


class Chest:
    """Common loot containers to be randomly found across the map."""

    def __init__(self):
        self.name = "chest"
  
    def __str__(self):
        return self.name
  
    def random_loot(self):
        """Generates random loot, weighted to more common items."""
        x = random.random()
        if x < 0.50:
            # find gold 50% of the time
            self.loot = "gold"
        # find common items 37.5% of the time
        elif x < 0.59375:
            self.loot = "arrow"
        elif x < 0.6875:
            self.loot = items.Spear()
        elif x < 0.78125:
            self.loot = items.Shield()
        elif x < 0.875:
            self.loot = items.Food()
        # find rare items 12.5% of the time
        elif x < 0.90625:
            self.loot = items.Dagger()
        elif x < 0.9375:
            self.loot = items.Bow()
        elif x < 0.96875:
            self.loot = items.Armor()
        elif x < 1.00:
            self.loot = items.Medicine()
        return self.loot
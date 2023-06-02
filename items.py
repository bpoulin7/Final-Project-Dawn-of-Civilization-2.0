# Items module - contains all items that can be stored in player's inventory


class Item:
    """An item that can be put into a player's inventory."""
  
    def __init__(self):
        self.name = None

    def __str__(self):
        return self.name

class Weapon(Item):
    """An item that deals damage to enemies in combat."""
  
    def __init__(self):
        self.damage = 0

class Spear(Weapon):
    """A weapon that does 25 damage."""
  
    def __init__(self):
        self.damage = 25
        self.name = "spear"
        self.desc = "a basic hand-held weapon"

class Dagger(Weapon):
    """A weapon that does 50 damage."""
  
    def __init__(self):
        self.damage = 50
        self.name = "dagger"
        self.desc = "a rare hand-held weapon"

class Bow(Weapon):
    """A weapon that requires arrows for input and does 10 damage."""
    def __init__(self):
        self.damage = 10
        self.name = "bow"
        self.desc = "a long-range weapon that requires arrows to work"

class Protection(Item):
    """An item that reduces damage dealt by enemies in combat."""
  
    def __init__(self):
        self.protection = 0

class Shield(Protection):
    """A protection item that lowers damage by 20."""
  
    def __init__(self):
        self.protection = 20
        self.name = "shield"
        self.desc = "a basic hand-held defense"

class Armor(Protection):
    """A protection item that permanently lowers damage by 45."""
  
    def __init__(self):
        self.protection = 45
        self.name = "armor"
        self.desc = "a rare full-body defense"

class Healing(Item):
    """An item that increases the player's hp."""
  
    def __init__(self):
        self.healing = 0

class Food(Healing):
    """A healing item that recovers 10 hp."""
  
    def __init__(self):
        self.healing = 10
        self.name = "food"
        self.desc = "rations to restore some hp"

class Medicine(Healing):
    """A healing item that recovers 25 hp."""
  
    def __init__(self):
        self.healing = 25
        self.name = "medicine"
        self.desc = "medicine to restore hp"


class Arrow(Item):
    """Ammo for bows."""
  
    def __init__(self):
        self.name = "arrow"
        self.desc = "ammo for a bow"
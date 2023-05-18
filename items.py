
class Item:
  def __init__(self):
    self.name = None
  def __str__(self):
    return self.name

class Weapon(Item):
  def __init__(self):
    self.damage = 0

class Spear(Weapon):
  def __init__(self):
    self.damage = 25
    self.name = "spear"
    self.desc = "a basic hand-held weapon"

class Dagger(Weapon):
  def __init__(self):
    self.damage = 50
    self.name = "dagger"
    self.desc = "a rare hand-held weapon"

class Bow(Weapon):
  def __init__(self):
    self.damage = 10
    self.name = "bow"
    self.desc = "a long-range weapon that requires arrows to work"

class Protection(Item):
  def __init__(self):
    self.protection = 0

class Shield(Protection):
  def __init__(self):
    self.protection = 20
    self.name = "shield"
    self.desc = "a basic hand-held defense"

class Armor(Protection):
  def __init__(self):
    self.protection = 45
    self.name = "armor"
    self.desc = "a rare full-body defense"

class Healing(Item):
  def __init__(self):
    self.healing = 0

class Food(Healing):
  def __init__(self):
    self.healing = 10
    self.name = "food"
    self.desc = "rations to restore some hp"

class Medicine(Healing):
  def __init__(self):
    self.healing = 25
    self.name = "medicine"
    self.desc = "medicine to restore hp"

class Water(Item):
  def __init__(self):
    self.thirst = 25
    self.name = "water"
    self.desc = "water to restore stamina"

class Arrow(Item):
  def __init__(self):
    self.name = "arrow"
    self.desc = "ammo for a bow"
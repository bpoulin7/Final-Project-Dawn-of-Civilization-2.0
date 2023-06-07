# Enemy module - contains all possible enemies to be encountered


class Enemy:
    """Hostile NPCs to be randomly found around the map."""

    def __init__(self):
        raise NotImplementedError("Enemy needs to be defined")
  
    def __str__(self):
        return self.name
  
    def is_alive(self):
        return self.hp > 0


class Spearman(Enemy):
    """Common enemy, equivalent to player using spear and shield."""

    def __init__(self):
        self.name = "spearman"
        self.hp = 100
        self.damage = 25


class Archer(Enemy):
    """Common enemy, equivalent to player using bow and arrows."""

    def __init__(self):
        self.name = "archer"
        self.hp = 100
        self.damage = 10


class Mercenary(Enemy):
    """Rare enemy, equivalent to player using dagger and armor."""

    def __init__(self):
        self.name = "mercenary"
        self.hp = 200
        self.damage = 50


class Thief(Enemy):
    """Common enemy, easy to defeat."""

    def __init__(self):
        self.name = "thief"
        self.hp = 50
        self.damage = 10
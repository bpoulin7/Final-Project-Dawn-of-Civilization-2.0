# Player module - contains all elements specific to the player

import items, mapobjects, characters
import random


class Player:
    """Contains inventory, hp, location, movement, actions, and events."""

    def __init__(self, x, y):
        self.inventory = [items.Spear(), items.Food(), items.Bow(),
                          items.Arrow(), items.Arrow(), items.Armor(),
                          items.Shield()]
        self.gold = 0
        # starts with no items and no gold
        self.prestige = 0
        # starts with no prestige
        self.hp = 100
        # starts with full health
        self.x = x
        self.y = y
        self.victory = False

    def is_alive(self):
        """Displays whether player has any remaining health points."""
        return self.hp > 0
  
    def print_inventory(self):
        """Lists items currently in player inventory, and current gold."""
        print("\nInventory:")
        if self.inventory:
            for item in self.inventory:
                print(f" - {item}")
        else:
            print("You don't have anything in your inventory!")
        print(f"Gold: {self.gold}")
        print(f"Prestige: {self.prestige}")
        print(f"Health: {self.hp}")

# Functions for random occurrences # -----------------------------------------
  
    def found_map_object(self, obj):
        """Procedure for interacting with map objects."""
        print(f"\nYou found a {obj.__str__()}.")
        collect_input = input("Do you want to collect loot? ").lower()
        if collect_input == "y" or collect_input == "yes":
            new_item = obj.random_loot()
            if new_item == "gold":
                g = int(random.random() * 100)
                self.gold = self.gold + g
                print(f"\nYou found {g} gold!")
            else:
                self.inventory.append(new_item)
                print(f"\nYou found a {new_item.__str__()}!")
        elif collect_input == "n" or collect_input == "no":
            return
        else:
            print("Invalid choice, try again.")
            self.found_map_object(obj)
  
    def random_map_object(self):
        """Generates chance of encountering map objects."""
        r = random.random()
        if r <= 0.5:
            # 50% chance of finding a chest upon moving
            self.found_map_object(mapobjects.Chest())

    def random_event(self):
        """Generates chance of encountering random events."""
        r = random.random()
        if r <= 0.5:
            # 50% chance of event upon moving
            return
        elif r <= 0.55:
            self.comet_event()
        elif r <= 0.6:
            self.bridgekeeper_event()
        elif r <= 0.65:
            self.good_reputation_event()
        elif r <= 0.7:
            self.bad_reputation_event()
        elif r <= 0.75:
            self.generous_donation_event()
        elif r <= 0.8:
            return # TBA
        elif r <= 0.85:
            return # TBA
        elif r <= 0.9:
            return # TBA
        elif r <= 0.95:
            return # TBA
        elif r < 1:
            return # TBA

    def random_enemy(self):
        """Generates chance of encountering enemies."""
        r = random.random()
        if r <= 0.5:
            # 50% chance of encountering enemy upon moving
            return
        elif r <= 0.65:
            # 15% chance of spearman
            print("\nOh no! You have been attacked by a spearman!")
            self.battle(characters.Spearman())
        elif r <= 0.8:
            # 15% chance of thief
            print("\nOh no! You have been attacked by a thief!")
            self.battle(characters.Thief())
        elif r <= 0.95:
            # 15% chance of archer
            print("\nOh no! You have been attacked by an archer!")
            self.battle(characters.Archer())
        elif r <= 1:
            # 5% chance of mercenary
            print("\nOh no! You have been attacked by a mercenary!")
            self.battle(characters.Mercenary())

# Functions for movement # ---------------------------------------------------
  
    def move(self, dx, dy):
        """Defines player movement."""
        self.x += dx
        self.y += dy
        Player.random_map_object(self)
        Player.random_event(self)
        Player.random_enemy(self)
  
    def move_north(self):
        """Defines player movement up/north."""
        self.move(dx=0, dy=-1)
  
    def move_east(self):
        """Defines player movement right/east."""
        self.move(dx=1, dy=0)
  
    def move_south(self):
        """Defines player movement down/south."""
        self.move(dx=0, dy=1)
  
    def move_west(self):
        """Defines player movement left/west."""
        self.move(dx=-1, dy=0)

    def check_gameover(self):
      """Function to allow player confirmation to quit game."""
      check = input("Are you sure you want to exit game? ").lower()
      if check == "yes" or check == "y":
          self.gameover()
      elif check != "no" and check != "n":
          print("Invalid input")
          self.check_gameover()
  
    def gameover(self):
        """Function for ending game (victory or loss).
        Displays final score.
        """
        print("\nGame Over!")
        print(f"Gold: {self.gold}")
        print(f"Prestige: {self.prestige}")
        self.victory = True
  
# Functions for game interactions # ------------------------------------------
  
    def heal(self):
        """Checks for consumable items and uses if possible."""
        # finds consumable items in player inventory
        consumables = [item for item in self.inventory if
                       isinstance(item, (items.Food, items.Medicine))]
        # prevents healing if no consumables are found
        if not consumables:
            print("\nYou don't have any healing items!")
            return
        # prints a list of available consumable items
        print("Choose an item to use to heal:")
        for i, item in enumerate(consumables, 1):
            print("{}. {}".format(i, item))
        # takes the chosen consumable from the inventory and restores hp
        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")        
  
    def battle(self, enemy):
        """Battle against enemies"""
        battle_options = ["a", "d", "f", "q"]
        print("a - attack")
        if items.Shield() in self.inventory:
            print("d - defend")
        print("f - flee")
        print("q - quit game")
        battle_action = input("What do you want to do? ").lower()
        if battle_action in battle_options:
            if battle_action == "a":
                self.attack(enemy)
            elif battle_action == "d":
                if items.Shield() in self.inventory:
                    self.defend(enemy)
                else:
                    print("You don't have a shield!")
                    self.battle(enemy)
            elif battle_action == "f":
                self.flee(enemy)
            elif battle_action == "q":
                self.check_gameover()
        else:
            print("Invalid choice! Try again.")
            self.battle(enemy)
        
    def enemy_attack(self, enemy):
        """Attack from enemy."""
        if items.Armor() in self.inventory:
            self.hp += items.Armor().protection
        self.hp -= enemy.damage
        print(f"\n{enemy.name.title()} attacked!")
        if not self.is_alive():
            self.gameover()
        else:
            print(f"You have {self.hp} hp.\n")
            self.battle(enemy)
  
    def attack(self, enemy):
        """Deal damage to enemies."""
        weapons = [item for item in self.inventory if
                   isinstance(item, items.Weapon)]
        if not weapons:
            print("\nYou don't have any weapons!")
            self.flee(enemy)
        else:
            print("\nChoose a weapon to use:")
            for i, item in enumerate(weapons, 1):
                print(f"{i}. {item}")
            choice = input("")
            try:
                to_use = weapons[int(choice) - 1]
                if to_use == items.Bow():
                    arrows = [item for item in self.inventory
                              if isinstance(items.Arrow)]
                    if not arrows:
                        print("You don't have any arrows!")
                    else:
                        to_shoot = arrows[1]
                        self.inventory.remove(to_shoot)
                        enemy.hp -= to_use.damage
                        if not enemy.is_alive():
                            print("\nVictory! Gain 25 prestige.")
                            self.prestige += 25
                        else:
                            print(f"{enemy.name.title()} has {enemy.hp} hp.")
                else:
                    enemy.hp -= to_use.damage
                    if not enemy.is_alive():
                        print("\nVictory! Gain 25 prestige.")
                        self.prestige += 25
                    else:
                        print(f"{enemy.name.title()} has {enemy.hp} hp.")
            except(ValueError, IndexError):
                print("Invalid choice, try again.")
            if enemy.is_alive() == True:
                self.enemy_attack(enemy)

    def defend(self, enemy):
        self.hp = min(100, self.hp + items.Shield().protection)
        self.enemy_attack(enemy)

    def flee(self, enemy):
        print("\nRun away!")
        print("Lose 50% prestige.")
        self.prestige = int(self.prestige / 2)

# Functions for events # -----------------------------------------------------
  
    def comet_event(self):
        print("\nComet Sighted!")
        print("A streak of light flashes across the night sky.")
        print("What does this mean?")
        print("\n1 - It's an omen! (lose 25% health points)")
        print("2 - Send gold to appease the comet! (lose 25% gold)")
        print("3 - I don't care. (lose 25% prestige)")
        playerinput = input("")
        if playerinput == "1":
            self.hp -= int(0.25 * self.hp)
        elif playerinput == "2":
            self.gold -= int(0.25 * self.gold)
        elif playerinput == "3":
            self.prestige -= int(0.25 * self.prestige)
        else:
            print("Invalid choice!")
            self.comet_event()

    def bridgekeeper_event(self):
        print("\nThe Bridgekeeper")
        print("""In order to cross a bridge on your path, you must answer
        the bridgekeeper's question.""")
        question = random.random()
        if question <= 0.25:
            answer = input("'What... is the capital of Assyria?' ").lower()
            if answer == "assur" or answer == "ashur":
                print("Correct! You are free to cross the bridge.")
            else:
                print("Incorrect! Lose 50% health.")
                self.hp = int(self.hp * 0.5)
        elif question <= 0.5:
            answer = input("""'What... is the flight speed of an unladen
            swallow?' """)
            if "European" in answer and "African" in answer:
                print("'Well I don't know...'")
                print("You are free to cross the bridge.")
            else:
                print("Incorrect! Lose 50% health.")
                self.hp = int(self.hp * 0.5)
        elif question <= 0.75:
            answer = input("'What... is your favourite color?' ")
            print("Correct! You are free to cross the bridge.")
        elif question <= 1:
            answer = input("'What... is the opposite of wheat?' ").lower()
            if answer == "cornflower":
                print("Correct! You are free to cross the bridge.")
            else:
                print("Incorrect! Lose 50% health.")
                self.hp = int(self.hp * 0.5)

    def good_reputation_event(self):
        print("\nGood Reputation")
        print("Word has gotten around about you - and it's good!")
        print("Gain 10 prestige.")
        self.prestige += 10

    def bad_reputation_event(self):
        print("\nBad Reputation")
        print("Word has gotten around about you - and it's not good.")
        print("Lose 10 prestige.")
        self.prestige -= 10

    def generous_donation_event(self):
        print("\nA Generous Donation")
        print(f"""The {self.allegiance.adjective} ruler has decided to fund
        your excursion.""")
        print("Gain 50% gold!")
        self.gold = int(self.gold * 1.5)
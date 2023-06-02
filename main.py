import map, items, player, characters

def play():
    """Function that contains all gameplay."""
    while player.is_alive() and not player.victory:
        # actual gameplay while player is active
        # displays information about current location
        currloc = map.location(player.x, player.y)
        if (currloc.name == "desert" or currloc.name == "mountains" or
            currloc.name == "sea"):
            print(f"\n{currloc.desc}")
        else:
            print(f"\nYou are in {currloc.__str__().title()}, {currloc.desc}")
        northloc = map.location(player.x, player.y - 1)
        eastloc = map.location(player.x + 1, player.y)
        southloc = map.location(player.x, player.y + 1)
        westloc = map.location(player.x - 1, player.y)
        if player.is_alive() and not player.victory:
            # displays possible actions and hotkeys based on current position
            if player.y > 0:
                if northloc != None:
                    if (northloc.name != "desert" and northloc.name
                        != "mountains"
                        and northloc.name != "sea"):
                        print("n - go north")
            if player.x < 9:
                if eastloc != None:
                    if (eastloc.name != "desert" and eastloc.name
                        != "mountains" and eastloc.name != "sea"):
                        print("e - go east")
            if player.y < 9:
                if southloc != None:
                    if (southloc.name != "desert" and southloc.name
                        != "mountains" and southloc.name != "sea"):
                        print("s - go south")
            if player.x > 0:
                if westloc != None:
                    if (westloc.name != "desert" and westloc.name
                        != "mountains" and westloc.name != "sea"):
                        print("w - go west")
            print("i - open inventory")
            print("m - open minimap")
            if player.hp < 100:
                print("h - heal")
            print("q - quit")
            action_input = get_action()
            if action_input == "n" and player.y > 0:
                if northloc != None:
                    if (northloc.name != "desert" and northloc.name
                        != "mountains" and northloc.name != "sea"):
                        player.move_north()
                    else:
                        print(f"""There is impassable {northloc.name}
                        to the north.""")
                else:
                    print("You can't go that way!")
            elif action_input == "e" and player.x < 9:
                if eastloc != None:
                    if (eastloc.name != "desert" and eastloc.name
                        != "mountains" and eastloc.name != "sea"):
                        player.move_east()
                    else:
                        print(f"""There is impassable {eastloc.name}
                        to the east.""")
                else:
                    print("You can't go that way!")
            elif action_input == "s" and player.y < 9:
                if southloc != None:
                    if (southloc.name != "desert" and southloc.name
                        != "mountains" and southloc.name != "sea"):
                        player.move_south()
                    else:
                        print(f"""There is impassable {southloc.name}
                        to the south.""")
                else:
                    print("You can't go that way!")
            elif action_input == "w" and player.x > 0:
                if westloc != None:
                    if (westloc.name != "desert" and westloc.name
                        != "mountains" and westloc.name != "sea"):
                        player.move_west()
                    else:
                        print(f"""There is impassable {southloc.name}
                        to the south.""")
                else:
                    print("You can't go that way!")
            elif action_input == "i":
                player.print_inventory()
            elif action_input == "m":
                with open("minimap.txt") as file:
                    gamemap = file.read()
                print(gamemap)
            elif action_input == "h" and player.hp < 100:
                player.heal()
            elif action_input == "q":
                player.check_gameover()
            else:
                print("Invalid action")
        elif not player.is_alive():
            # ends play loop if hp reaches 0
            print("Oh no!")
            player.gameover(player)


def get_action():
    """Function for ease of returning player input for main actions."""
    return input("What would you like to do? ").lower()


print("Welcome to the Dawn of Civilization!")
print("It is the mid 16th century BCE in Mesopotamia.")
print("""You are going to be a warrior and adventurer, travelling around the
known world and trying to earn Gold and Prestige.""")
print("""Along the way, you may find treasure, equipment, and enemies, and
will be greeted with both good and bad events.\n""")
print("Choose a starting location:")
# write gamemap
with open("minimap.txt") as file:
    gamemap = file.read()
print(gamemap)
selected = False
while not selected:
    # allows player to select starting location
    startloc = input("").lower()
    if startloc == "troy":
        player = player.Player(0, 0)
        selected = True
    elif startloc == "hattusa":
        player = player.Player(1, 0)
        selected = True
    elif startloc == "samuha":
        player = player.Player(2, 0)
        selected = True
    elif startloc == "apasa":
        player = player.Player(0, 1)
        selected = True
    elif startloc == "kummanni":
        player = player.Player(1, 1)
        selected = True
    elif startloc == "meliddu":
        player = player.Player(2, 1)
        selected = True
    elif startloc == "lukka":
        player = player.Player(0, 2)
        selected = True
    elif startloc == "adana":
        player = player.Player(1, 2)
        selected = True
    elif startloc == "karkemish":
        player = player.Player(2, 2)
        selected = True
    elif startloc == "washukanni":
        player = player.Player(3, 2)
        selected = True
    elif startloc == "nineveh":
        player = player.Player(4, 2)
        selected = True
    elif startloc == "erbil":
        player = player.Player(5, 2)
        selected = True
    elif startloc == "ugarit":
        player = player.Player(1, 3)
        selected = True
    elif startloc == "emar":
        player = player.Player(2, 3)
        selected = True
    elif startloc == "tarqa":
        player = player.Player(3, 3)
        selected = True
    elif startloc == "ashur":
        player = player.Player(4, 3)
        selected = True
    elif startloc == "arrapkha":
        player = player.Player(5, 3)
        selected = True
    elif startloc == "byblos":
        player = player.Player(1, 4)
        selected = True
    elif startloc == "palmyra":
        player = player.Player(2, 4)
        selected = True
    elif startloc == "kurigalzu":
        player = player.Player(3, 4)
        selected = True
    elif startloc == "eshnunna":
        player = player.Player(4, 4)
        selected = True
    elif startloc == "tyre":
        player = player.Player(1, 5)
        selected = True
    elif startloc == "sippar":
        player = player.Player(4, 5)
        selected = True
    elif startloc == "upi":
        player = player.Player(5, 5)
        selected = True
    elif startloc == "ascalon":
        player = player.Player(1, 6)
        selected = True
    elif startloc == "jericho":
        player = player.Player(2, 6)
        selected = True
    elif startloc == "babylon":
        player = player.Player(4, 6)
        selected = True
    elif startloc == "kish":
        player = player.Player(5, 6)
        selected = True
    elif startloc == "nippur":
        player = player.Player(6, 6)
        selected = True
    elif startloc == "susa":
        player = player.Player(7, 6)
        selected = True
    elif startloc == "warhashi":
        player = player.Player(8, 6)
        selected = True
    elif startloc == "heliopolis":
        player = player.Player(0, 7)
        selected = True
    elif startloc == "avaris":
        player = player.Player(1, 7)
        selected = True
    elif startloc == "uruk":
        player = player.Player(6, 7)
        selected = True
    elif startloc == "liyan":
        player = player.Player(8, 7)
        selected = True
    elif startloc == "memphis":
        player = player.Player(0, 8)
        selected = True
    elif startloc == "ur":
        player = player.Player(6, 8)
        selected = True
    elif startloc == "anshan":
        player = player.Player(8, 8)
        selected = True
    else:
        print("Invalid choice! Try again.")
        selected = False

# assigns player's associated civilization based on starting location
player.allegiance = map.location(player.x, player.y).owner
# assigns player's starting prestige based on starting civilization
player.prestige = player.allegiance.prestige
# displays opening text based on starting location
temp_loc = map.location(player.x, player.y)
print(f"\nYou start in the city of {startloc.title()}, {temp_loc.desc}.\n")
print(f"You are loyal to the civilization of {player.allegiance},")
print(f"{player.allegiance.desc}\n")
print("Because of the size of your civilization, you get a starting bonus of {} prestige.".format(player.allegiance.prestige))
# displays starting inventory
print("You start with:")
print(player.print_inventory())


play()

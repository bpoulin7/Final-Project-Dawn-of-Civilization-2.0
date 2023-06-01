# Initial Plan: #

MAIN FILE:
```
print intro text  
pick start location:  
	start location = input  
		player coordinates = input coordinates  
game loop:  
	options menu:  
		list options (move n/s/e/w, open map/inventory, fight, quit, etc.)  
		action = input  
			perform action  
	upon movement:  
		random events  
			response = input  
				perform response  
		random objects  
			interact = input  
				perform interaction  
		random enemies  
			fight or flee = input  
				perform interaction  
				if battle:  
					weapon = input  
					option = input  
						perform option  
game over:  
	print outro text  
```

# List of Classes/Modules/Objects: #

- Player
- Map tiles (city, desert, mountain, sea)
- Civilizations
- Map objects
- Items
  - Weapons (spear, bow, arrow, dagger)
  - Protection (helmet, armor, shield)
  - Healing (water, food, medicine, maybe more)
- NPCs (soldier, archer, mercenary, maybe trader)
- Events

# Timeline: #

May 12 - start project  
May 17 - finish map  
May 19 - finish items and objects  
May 24 - finish enemies and battles  
May 26 - finish events and gameplay  
May 29 - αlpha testing  
May 31 - βeta testing  
June 2 - finish project
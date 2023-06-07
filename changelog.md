# Changelog

All notable changes to this project will be documented in this file

## 0.0.1 - 17/05/2023

 - Added all modules presumed to be necessary
 - Added Location and Civilization classes and objects to map module

## 0.0.2 - 18/05/2023

- Added Item classes and subclasses: spear, dagger, and bow Weapons; shield
  and armor Protection; food and medicine Healing; water; and arrows

## 0.0.3 - 19/05/2023

 - Transferred changelog, development, and proposal files to Replit after
   being unable to merge with GitHub
 - Copied player module from previous project

## 0.0.4 - 23/05/2023

 - added Enemy classes

## 0.0.5 - 24/05/2023

 - added battle functions

## 0.0.6 - 25/05/2023

 - started adding Events
 - started adding ability for player to select starting location

## 0.0.7 - 26/05/2023

 - added missing map functions, classes, objects, parameters, and arrays

## 0.0.8 - 27/05/2023

 - added `play` function
 - added some missing locations and descriptions

## 0.0.9 - 29/05/2023

 - fixed much of console text display issues
 - added map objects

## 0.0.10 - 30/05/2023

 - added remainder of of battle gameplay
 - moved `game over` function from main to player module
 - fixed bug in heal menu that prevented healing items from being selected
 - decided to avoid adding special gameplay to escape deserts
   - instead modified movement functions to completely prevent movement into desert, mountain, or sea tiles

## 0.0.11 - 31/05/2023

 - attempted to add functionality for bow and arrow, but encountering bugs
 - fixed bug where healing during battle would exit the battle
 - removed some code that was going to be important, now deemed unnecessary
 - added very temporary minimap
 - added comments to main file
 - formatted items file
 - restricted "heal" option to only be available when hp is not already full
 - added remaining location descriptions

## 0.0.12 - 01/06/2023 (Alpha)

 - moved minimap to external file to be written in

## 0.1.0 - 01/06/2023

 - fixed error caused by being in location next to map border
 - fixed formatting in items, map, and player modules and main file
 - removed ability to heal in battle
 - converted all multiplied and divided gold and prestige values into integers
 - removed placeholder answer in "Bridgekeeper" event question
 - added more information in starting text
 - added function to allow player to confirm exit game

## 0.1.1 - 02/06/2023

 - prevented use of shield in combat if player does not have one
 - removed potential for loot chests to have more than one item
 - added header to main file

## 0.1.2 - 03-04/06/2023

 - fixed more formatting in console output
 - attempted to prevent duplicate items in inventory
 - changed Arrows from class to integer value
 - added "Broken Item", "Royal Decree", "The Chasm", "Disease", and "The River" events
 - fixed west movement function having references to "south"
 - prevented hp and prestige values from dropping below 0

## 0.1.3 - 05/06/2023

 - complete fix of formatting
 - added comments where necessary
 - fixed another reference to "south" in west movement function
 - fixed incorrect coordinates of Kurigalzu and Eshnunna in starting location selection
 - fixed food and medicine not being recognized as stackable items

## 0.1.4 - 06/06/2023

 - added compass, border, legend, and title to minimap
 - used concatenation to resolve some text strings being too long
 - fixed bug that prevented "defend" option from appearing in battle menu
 - fixed bug that allowed defending to result in a net increase of hp
   - removed `enemy_attack` function, incorporated into `attack` and `defend`
 - fixed code to prevent duplicate items other than food and medicine
 - fixed code to get bows to consume arrows upon use
 - added damage reduction when armor is in inventory
 - made sure no events or battles can occur if hp reaches 0 before the play loop ends
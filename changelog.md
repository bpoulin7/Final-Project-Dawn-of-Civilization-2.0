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

 - added *play* function
 - added some missing locations and descriptions

## 0.0.9 - 29/05/2023

 - fixed much of console text display issues
 - added map objects

## 0.0.10 - 30/05/2023

 - added remainder of of battle gameplay
 - moved *game over* function from main to player module
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

## 0.1.0 - 01/06/2023 (Post Alpha)

 - fixed error caused by being in location next to map border
 - fixed formatting in items, map, and player modules and main file
 - removed ability to heal in battle
 - converted all multiplied and divided gold and prestige values into integers
 - removed placeholder answer in "Bridgekeeper" event question
 - added more information in starting text
 - added function to allow player to confirm exit game
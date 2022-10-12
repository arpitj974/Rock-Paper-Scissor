# Rock Paper Scissor Game
This project is an implementation of the traditional Rock Paper Scissor game using Python.This is a terminal based game : 


## Introduction



**The Aim of the project is as follows:**
+ The game explains rules to the players, and then asks them to make a choice.
+ Then the computer makes a random choice.
+ The game has conditions for winning and losing.
+ When the game is over, the player is asked if he/she wants to play again.
+ The player can play any number of games in one session.
+ The game finally displays overall results when the user ends the session

## Requirements to play the game
+ Python 3.8

## Instructions to Play 
+ Download the game files in a directory
+ In this directory, use terminal to run the game with the following command 
```python main.py```

## Instruction to run unit tests
+ Go to project directory and install requirements with the folllowing command ```pip install -r reqirements_dev.txt```
+ Run command from the project directory ```py.test```

## Configuration
+ The config.py file contains all the configurable knobs
+ Logging configuration such as log level, log file name, log file size etc can be configured here

## Running with Debug log level
+ By default, the log level is set to INFO
+ To run with debug log level, set log_level = "debug" in config.py file


## Log collection
+ Logs will be collected in game.log file in the same directory
 
### Additional features successfully implemented:
+ Validation of user's input without crashing the game.
+ Logging of all necessary events as per different log levels in game.log file



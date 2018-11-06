#! /usr/bin/env python3
# coding: utf-8

from level import Level
from character import Character

def main():
    print("Welcome !")
    print("Help McGyver to escape the labyrinth !")
    print("Grab the 3 objects and find the exit to beat the guardian...")

    """ Creation of the labyrinth"""
    level = Level()
    level.map_generator("file_map.txt")

    """ Initialisation of the character """
    mcgyver = Character(1, 0)
    
    continue_game = True

    """ Game Starts """
    while continue_game:
        action = input("Make McGyver move by using 'z', 's', 'w', or 'q' :")
        action.lower()

        try:
            assert action == 'z' or action == 's' or action == 'w' or action == 'q'
        except AssertionError:
            print("Wrong value")
        
        

if __name__ == "__main__":
    main()

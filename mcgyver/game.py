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
    level.map_generator()

    """ Initialisation of the character """
    mcgyver = Character(1, 0, level)
    
    continue_game = True

    """ Game Starts """
    while continue_game:

        mcgyver.move()


if __name__ == "__main__":
    main()

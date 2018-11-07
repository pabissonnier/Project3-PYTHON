#! /usr/bin/env python3
# coding: utf-8

from level import Level
from character import Character
from objects import Objects


def main():
    print("Welcome !")
    print("Help McGyver to escape the labyrinth !")
    print("Grab the 3 objects and find the exit to beat the guardian...")

    """ Creation  of the labyrinth"""
    level = Level()
    level.map_generator()

    """ Initialisation of the character """
    mcgyver = Character(0, 1, level)
    
    continue_game = True

    """ Game Starts """
    while continue_game:
        level.map_printer()
        mcgyver.move()
        mcgyver.mac_out()

    print("Bye bye !!")


if __name__ == "__main__":
    main()

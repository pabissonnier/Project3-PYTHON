#! /usr/bin/env python3
# coding: utf-8

from character import Character
from level import Level
from objects import Objects


def main():
    print("Welcome !")
    print("Help McGyver to escape the labyrinth !")
    print("Grab the 3 objects and find the exit to beat the guardian...")

    """ Creation  of the labyrinth and """
    level = Level()
    level.map_generator()

    """ Initialisation of the objects """
    needle = Objects('N', level)
    needle.rand_position()
    tube = Objects('T', level)
    tube.rand_position()
    ether = Objects('E', level)
    ether.rand_position()

    """ Initialisation of the character """
    mcgyver = Character(0, 1, level)

    continue_game = True

    while continue_game:
        """ Game starts """
        level.map_printer()
        mcgyver.move()
        if mcgyver.mac_out() is True:
            continue_game = True
        elif mcgyver.mac_out() is False:
            continue_game = False

    else:
        print("Bye bye !!")


if __name__ == "__main__":
    main()

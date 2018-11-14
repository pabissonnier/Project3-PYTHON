#! /usr/bin/env python3
# coding: utf-8

from level import Level


def main():
    print("Welcome !")
    print("Help McGyver to escape the labyrinth !")
    print("Grab the 3 objects and find the exit to beat the guardian...")

    level, mcgyver = Level.map_reset()

    continue_game = True

    while continue_game:

        # Game starts
        level.map_printer()
        mcgyver.move()

        # McGyver gets an object
        mcgyver.get_object(mcgyver.pos_x, mcgyver.pos_y)

        # McGyver gets out (or not)
        mcgyver.mac_out(mcgyver.pos_x, mcgyver.pos_y)

        # Leave game or not
        if mcgyver.end_game is False and mcgyver.win is True:
            print("Help McGyver to escape the labyrinth !")
            print("Grab the 3 objects and find the exit to beat the guardian...")
            level, mcgyver = Level.map_reset()

        elif mcgyver.end_game is True:
            continue_game = False

    print("GAME OVER, Bye bye !!")


if __name__ == "__main__":
    main()

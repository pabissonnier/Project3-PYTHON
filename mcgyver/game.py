#! /usr/bin/env python3
# coding: utf-8

from level import Level
from constants import *

import pygame
from pygame import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((sprites*sprite_size, sprites*sprite_size))
    pygame.display.set_caption(title_welcome)

    level, mcgyver = Level.map_reset()
    





    continue_game = True

    while continue_game:

        pygame.time.Clock().tick(30)

        # Game starts
        level.map_draw(screen)
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

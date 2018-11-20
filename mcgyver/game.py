#! /usr/bin/env python3
# coding: utf-8

from level import Level
from constants import *

import pygame
from pygame.locals import *

from character import Character


def main():
    pygame.init()
    screen = pygame.display.set_mode((sprites*sprite_size, sprites*sprite_size))
    pygame.display.set_caption(title_welcome)

    game_activated = True

    while game_activated:
        welcome = pygame.image.load(welcome_mac).convert()
        screen.blit(welcome, (100, 100))

        pygame.display.flip()

        continue_game = True
        continue_title = True

        # WELCOME LOOP
        while continue_title:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continue_title = False
                    continue_game = False
                    game_activated = False

                elif event.type == KEYDOWN and event.key == K_RETURN:
                    continue_title = False
                    # MAP AND ELEMENTS ARE GENERATED
                    """level, mcgyver, guardian = Level.map_reset()
                    level.map_draw(screen)
                    screen.blit(mcgyver, (0*sprite_size, 1*sprite_size))
                    screen.blit(guardian, (13*sprite_size, 14*sprite_size))
                    level.map_draw(screen)"""
                    level = Level()
                    level.map_generator()
                    level.map_draw(screen)
                    mcgyver = Character(0, 1, image_mcgyver, level)
                    guardian = Character(13, 14, image_guardian, level)
                    pygame.display.flip()

        while continue_game:
            # Game starts
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    continue_game = False
                    game_activated = False

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continue_game = False

                else:
                    mcgyver.move()
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

    pygame.quit()


if __name__ == "__main__":
    main()

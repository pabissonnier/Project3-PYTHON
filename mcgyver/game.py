#! /usr/bin/env python3
# coding: utf-8

from level import Level
from objects import Objects
from character import Character
from constants import *

import pygame
from pygame.locals import *


def main():
    # Pygame init
    pygame.init()
    screen = pygame.display.set_mode((sprites*sprite_size, sprites*sprite_size))

    icon = pygame.image.load(image_mcgyver)
    pygame.display.set_icon(icon)
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

                    # MAP IS CREATED
                    level = Level()
                    background = pygame.image.load(image_background).convert()
                    level.map_generator()
                    level.map_draw(screen)

                    # CHARACTERS ARE CREATED
                    mcgyver = Character(0, 1, image_mcgyver, level)
                    mcgyver.display(screen)
                    guardian = Character(14, 13, image_guardian, level)
                    guardian.display(screen)

                    # OBJECTS ARE CREATED
                    needle = Objects('N', image_needle, level)
                    needle.display(screen)
                    ether = Objects('E', image_ether, level)
                    ether.display(screen)
                    tube = Objects('T', image_tube, level)
                    tube.display(screen)

                    pygame.display.flip()

        # GAME LOOP
        while continue_game:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    continue_game = False
                    game_activated = False

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continue_game = False
                    elif event.key == K_RIGHT:
                        mcgyver.move("right")
                    elif event.key == K_DOWN:
                        mcgyver.move("down")
                    elif event.key == K_LEFT:
                        mcgyver.move("left")
                    elif event.key == K_UP:
                        mcgyver.move("up")
                    else:
                        print("Invalid key")

                    mcgyver.display(screen)

                    #mcgyver.get_object(mcgyver.pos_x, mcgyver.pos_y)

                    # McGyver gets out (or not)
                    #mcgyver.mac_out(mcgyver.pos_x, mcgyver.pos_y)

                # REFRESH SCREEN
                screen.blit(background, (0, 0))
                level.map_draw(screen)
                screen.blit(mcgyver.visual, (mcgyver.pos_x * sprite_size, mcgyver.pos_y * sprite_size))
                screen.blit(needle.im, (needle.obj_x * sprite_size, needle.obj_y * sprite_size))
                screen.blit(tube.im, (tube.obj_x * sprite_size, tube.obj_y * sprite_size))
                screen.blit(ether.im, (ether.obj_x * sprite_size, ether.obj_y * sprite_size))
                pygame.display.flip()





            # Leave game or not
            if mcgyver.end_game is False and mcgyver.win is True:
                print("Help McGyver to escape the labyrinth !")
                print("Grab the 3 objects and find the exit to beat the guardian...")
                level, mcgyver = Level.map_reset()

            elif mcgyver.end_game is True:
                continue_game = False

            pygame.display.flip()

        print("GAME OVER, Bye bye !!")

    pygame.quit()


if __name__ == "__main__":
    main()

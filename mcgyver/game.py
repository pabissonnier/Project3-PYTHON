#! /usr/bin/env python3
# coding: utf-8

from level import Level
from objects import Objects
from character import Character
from constants import *

import pygame
from pygame.locals import *


def main():
    game_activated = True
    while game_activated:

        # SCREEN LOADING
        pygame.init()
        screen = pygame.display.set_mode((sprites*sprite_size, sprites*sprite_size + 50))
        icon = pygame.image.load(image_mcgyver)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(title_welcome)

        # WELCOME PAGE LOADING
        welcome = pygame.image.load(welcome_mac).convert()
        screen.blit(welcome, (100, 100))

        pygame.display.flip()

        continue_game = True
        continue_title = True
        continue_instructions = True

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
                    guardian = Character(14, 13, image_guardian, level)

                    # OBJECTS ARE CREATED
                    needle = Objects('N', image_needle, level)
                    ether = Objects('E', image_ether, level)
                    tube = Objects('T', image_tube, level)

                    pygame.display.flip()

        # INSTRUCTIONS LOOP
        while continue_instructions:
            pygame.time.Clock().tick(30)

            instructions = pygame.image.load(image_instructions).convert()
            screen.blit(instructions, (0, 0))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continue_title = False
                    continue_game = False
                    game_activated = False

                elif event.type == KEYDOWN and event.key == K_RETURN:
                    continue_instructions = False

        # GAME LOOP
        while continue_game:
            pygame.time.Clock().tick(30)

            # REFRESH SCREEN
            screen.blit(background, (0, 0))
            level.map_draw(screen)
            screen.blit(mcgyver.visual, (mcgyver.pos_x * sprite_size, mcgyver.pos_y * sprite_size))
            screen.blit(guardian.visual, (guardian.pos_x * sprite_size, guardian.pos_y * sprite_size))

            # INVENTORY
            instructions = pygame.image.load(image_instructions).convert()
            screen.blit(instructions, (0, 0))


            for line in level.map:
                for case in line:
                    if "N" in case:
                        screen.blit(needle.im, (needle.obj_x * sprite_size, needle.obj_y * sprite_size))
                    if "T" in case:
                        screen.blit(tube.im, (tube.obj_x * sprite_size, tube.obj_y * sprite_size))
                    if "E" in case:
                        screen.blit(ether.im, (ether.obj_x * sprite_size, ether.obj_y * sprite_size))

            pygame.display.flip()

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

            # Show inventory
            if len(mcgyver.items) != 0:
                pass

            # Mcgyver wins or not
            if mcgyver.mac_out(mcgyver.pos_x, mcgyver.pos_y) is False:
                print("You lose !")


            # Leave game or not
            """if mcgyver.end_game is False:
                print("Help McGyver to escape the labyrinth !")
                print("Grab the 3 objects and find the exit to beat the guardian...")
                continue_game = False

            elif mcgyver.end_game is True:
                print("GAME OVER, Bye bye !!")
                continue_game = False
                game_activated = False
                pygame.quit()"""


if __name__ == "__main__":
    main()

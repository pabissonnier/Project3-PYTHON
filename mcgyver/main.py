#!/usr/bin/env python3

from level import Level
from objects import Objects
from character import Character
from constants import *

import pygame
from pygame.locals import *


def main():
    game_activated = True
    while game_activated:
        pygame.time.Clock().tick(30)
        # SCREEN LOADING
        pygame.init()
        screen = pygame.display.set_mode((SPRITES * SPRITE_SIZE, SPRITES * SPRITE_SIZE + 50))
        icon = pygame.image.load(IMAGE_MCGYVER).convert()
        pygame.display.set_icon(icon)
        pygame.display.set_caption(TITLE_WELCOME)

        # MUSIC LOADING
        sound_mac_theme = pygame.mixer.Sound(MAC_THEME)

        # WELCOME PAGE LOADING
        welcome = pygame.image.load(WELCOME_MAC).convert()
        screen.blit(welcome, (0, 0))

        pygame.display.flip()

        continue_game = True
        continue_title = True
        continue_instructions = True

        # WELCOME LOOP
        while continue_title:


            sound_mac_theme.play()

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)\
                        or (event.type == KEYDOWN and event.key == K_SPACE):
                    pygame.quit()
                    exit()

                elif event.type == KEYDOWN and event.key == K_RETURN:
                    continue_title = False
                    sound_mac_theme.stop()

                    # MAP IS CREATED
                    level = Level()
                    background = pygame.image.load(IMAGE_BACKGROUND).convert()
                    level.map_generator()

                    # CHARACTERS ARE CREATED
                    mcgyver = Character(0, 1, IMAGE_MCGYVER, level)
                    guardian = Character(14, 13, IMAGE_GUARDIAN, level)

                    # OBJECTS ARE CREATED
                    needle = Objects('N', IMAGE_NEEDLE, level)
                    ether = Objects('E', IMAGE_ETHER, level)
                    tube = Objects('T', IMAGE_TUBE, level)

                    pygame.display.flip()

        # INSTRUCTIONS LOOP
        while continue_instructions:
            #pygame.time.Clock().tick(30)

            instructions = pygame.image.load(IMAGE_INSTRUCTIONS).convert()
            screen.blit(instructions, (0, 0))

            inventory = pygame.image.load(IMAGE_INVENTORY).convert()
            screen.blit(inventory, (0, 600))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_SPACE:
                    pygame.quit()
                    exit()

                elif event.type == KEYDOWN and event.key == K_RETURN:
                    continue_instructions = False

        # GAME LOOP
        while continue_game:
            #pygame.time.Clock().tick(30)

            # REFRESH SCREEN
            screen.blit(background, (0, 0))
            level.map_draw(screen)

            screen.blit(mcgyver.visual, (mcgyver.pos_x * SPRITE_SIZE, mcgyver.pos_y * SPRITE_SIZE))
            screen.blit(guardian.visual, (guardian.pos_x * SPRITE_SIZE, guardian.pos_y * SPRITE_SIZE))

            for line in level.map:
                for case in line:
                    if "N" in case:
                        screen.blit(needle.im, (needle.obj_x * SPRITE_SIZE, needle.obj_y * SPRITE_SIZE))
                    elif "T" in case:
                        screen.blit(tube.im, (tube.obj_x * SPRITE_SIZE, tube.obj_y * SPRITE_SIZE))
                    elif "E" in case:
                        screen.blit(ether.im, (ether.obj_x * SPRITE_SIZE, ether.obj_y * SPRITE_SIZE))

            # Games actions
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continue_game = False

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

            # INVENTORY DISPLAYING
            if ether.name in mcgyver.items:
                ether.rank_in_list(mcgyver, screen)
            if tube.name in mcgyver.items:
                tube.rank_in_list(mcgyver, screen)
            if needle.name in mcgyver.items:
                needle.rank_in_list(mcgyver, screen)

            # WINS OR DIES
            if mcgyver.win:
                mcgyver.game_over(screen)
                music_win = pygame.mixer.Sound(MAC_WIN)
                music_win.play()
                if mcgyver.finish_game:
                    pygame.quit()  # Message d'erreur
                elif mcgyver.start_again:
                    music_win.stop()
                    continue_game = False
            elif mcgyver.end_game:
                macgameover = pygame.image.load(MAC_GAMEOVER).convert()
                screen.blit(macgameover, (0, 0))
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_SPACE:
                        pygame.quit()
                    elif event.type == KEYDOWN and event.key == K_RETURN:
                        continue_game = False

            pygame.display.flip()


if __name__ == "__main__":
    main()

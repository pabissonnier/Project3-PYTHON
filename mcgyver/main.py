#!/usr/bin/env python3

from level import Level
from objects import Objects
from character import Character
from constants import *

import pygame


def main():
    """ Main function """

    game_activated = True

    while game_activated:

        """ Main loop containing 'Welcome loop', ' Instruction loop' and 'Game loop'.
        Initialization of all the game elements """

        pygame.time.Clock().tick(30)

        # SCREEN LOADING
        level = Level()
        pygame.init()
        screen = pygame.display.set_mode((SPRITES * SPRITE_SIZE, SPRITES * SPRITE_SIZE + 50))
        icon = pygame.image.load(IMAGE_MCGYVER).convert()
        pygame.display.set_icon(icon)
        pygame.display.set_caption(TITLE_WELCOME)

        # MUSIC LOADING
        sound_mac_theme = pygame.mixer.Sound(MAC_THEME)
        music_win = pygame.mixer.Sound(MAC_WIN)

        # MAP IS CREATED
        background = pygame.image.load(IMAGE_BACKGROUND).convert()

        # CHARACTERS ARE CREATEDpylin
        mcgyver = Character(0, 1, IMAGE_MCGYVER, level)
        guardian = Character(14, 13, IMAGE_GUARDIAN, level)

        # OBJECTS ARE CREATED
        needle = Objects('N', IMAGE_NEEDLE, level)
        ether = Objects('E', IMAGE_ETHER, level)
        tube = Objects('T', IMAGE_TUBE, level)

        # WELCOME PAGE LOADING AND SHOWING
        welcome = pygame.image.load(WELCOME_MAC).convert()
        screen.blit(welcome, (0, 0))

        # INSTRUCTION PAGE LOADING
        instructions = pygame.image.load(IMAGE_INSTRUCTIONS).convert()

        # INVENTORY AT THE BOTTOM OF THE SCREEN LOADING
        inventory = pygame.image.load(IMAGE_INVENTORY).convert()

        pygame.display.flip()

        continue_game = True
        continue_title = True
        continue_instructions = True

        # WELCOME LOOP
        while continue_title:

            sound_mac_theme.play()

            if level.player_decision():
                continue_title = False
            elif level.player_decision() is False:
                pygame.quit()
                exit()

                level.map_generator()

                pygame.display.flip()

        # INSTRUCTIONS LOOP
        while continue_instructions:
            sound_mac_theme.stop()
            screen.blit(instructions, (0, 0))
            screen.blit(inventory, (0, 600))

            if level.player_decision():
                continue_instructions = False
            elif level.player_decision() is False:
                pygame.quit()
                exit()

            pygame.display.flip()

        # GAME LOOP
        while continue_game:

            # Displaying map and refreshing screen
            screen.blit(background, (0, 0))
            level.map_draw(screen)
            screen.blit(mcgyver.visual, (mcgyver.pos_x * SPRITE_SIZE, mcgyver.pos_y * SPRITE_SIZE))
            screen.blit(guardian.visual, (guardian.pos_x * SPRITE_SIZE, guardian.pos_y * SPRITE_SIZE))

            # Displaying objects images for each objects position
            ether.displaying_objects(level, screen)
            tube.displaying_objects(level, screen)
            needle.displaying_objects(level, screen)

            # Games actions
            mcgyver.is_moving()
            if mcgyver.is_moving() is False:
                continue_game = False

            # Inventory displaying
            ether.display_in_inventory(mcgyver, screen)
            tube.display_in_inventory(mcgyver, screen)
            needle.display_in_inventory(mcgyver, screen)

            # MacGyver wins or loses
            mcgyver.wins_or_not(screen, music_win, level)
            if mcgyver.wins_or_not(screen, music_win, level) is False:
                continue_game = False

            pygame.display.flip()


if __name__ == "__main__":
    main()

""" Loading of Pygame"""
import pygame
from pygame.locals import *

from constants import SPRITE_SIZE, MAC_STEP, MAC_GETOBJECT, GUARDIAN_FIRE, OUT_MAC, MAC_GAMEOVER


class Character:
    """ Class to generate the characters """
    def __init__(self, ini_x, ini_y, image, labyrinth):
        self.pos_x = ini_x
        self.pos_y = ini_y
        self.x = self.pos_x * SPRITE_SIZE
        self.y = self.pos_y * SPRITE_SIZE
        self.level = labyrinth
        self.items = []
        self.visual = pygame.image.load(image).convert_alpha()
        self.end_game = False
        self.win = False
        self.start_again = False
        self.finish_game = False

    def is_moving(self):
        """ First function to move MacGyver, determines the keys to press """
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE \
                    or event.type == KEYDOWN and event.key == K_SPACE:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.move("right")
                elif event.key == K_DOWN:
                    self.move("down")
                elif event.key == K_LEFT:
                    self.move("left")
                elif event.key == K_UP:
                    self.move("up")
                else:
                    print("Invalid key")

    def move(self, direction):
        """ Second function to move MacGyver, it establishes the direction """
        if direction == "right" and self.level.check_new_coors(self.pos_x + 1, self.pos_y):
            self.do_move(self.pos_x + 1, self.pos_y)
        elif direction == "up" and self.level.check_new_coors(self.pos_x, self.pos_y - 1):
            self.do_move(self.pos_x, self.pos_y - 1)
        elif direction == "left" and self.level.check_new_coors(self.pos_x - 1, self.pos_y):
            self.do_move(self.pos_x - 1, self.pos_y)
        elif direction == "down" and self.level.check_new_coors(self.pos_x, self.pos_y + 1):
            self.do_move(self.pos_x, self.pos_y + 1)
        else:
            pass

    def do_move(self, new_x, new_y):
        """ Third function to move MacGyver, determines the actions while moving """
        self.get_object(new_x, new_y)
        self.mac_out(new_x, new_y)
        self.level.map[self.pos_y][self.pos_x] = ' '
        self.pos_x = new_x
        self.pos_y = new_y
        self.level.map[self.pos_y][self.pos_x] = 'M'
        sound_mac_move = pygame.mixer.Sound(MAC_STEP)
        sound_mac_move.play()

    def get_object(self, case_x, case_y):
        """ MacGyver gets an object when his coordinates correspond to a letter """
        sound_mac_getobject = pygame.mixer.Sound(MAC_GETOBJECT)
        if self.level.map[case_y][case_x] in "E":
            self.items.append("E")
            sound_mac_getobject.play()
        elif self.level.map[case_y][case_x] in "T":
            self.items.append("T")
            sound_mac_getobject.play()
        elif self.level.map[case_y][case_x] in "N":
            self.items.append("N")
            sound_mac_getobject.play()

    def mac_out(self, case_x, case_y):
        """ MacGyver gets out if he finds the exit and has 3 items in his inventory """
        if self.level.map[case_y][case_x] == "G":
            if len(self.items) >= 3:
                self.win = True
            else:
                sound_mac_killed = pygame.mixer.Sound(GUARDIAN_FIRE)
                sound_mac_killed.play()
                self.end_game = True

    def mac_wins(self, window):
        """ A new screen appears when MacGyver wins """
        image_game_over = pygame.image.load(OUT_MAC).convert()
        window.blit(image_game_over, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_SPACE \
                    or event.type == KEYDOWN and event.key == K_SPACE:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_RETURN:
                self.start_again = True

    def wins_or_not(self, window, music_win, maze):
        """ MacGyver gets out of the maze, there are two possibilities """
        if self.win:
            self.mac_wins(window)
            music_win.play()
            if self.start_again:
                music_win.stop()
                return False
        elif self.end_game:
            macgameover = pygame.image.load(MAC_GAMEOVER).convert()
            window.blit(macgameover, (0, 0))
            if maze.player_decision():
                return False
            elif maze.player_decision() is False:
                pygame.quit()
                exit()

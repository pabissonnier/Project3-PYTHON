import pygame
from pygame.locals import *
from constants import *


class Character:

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

    def display(self, window):
        window.blit(self.visual, (self.x, self.y))

    def move(self, direction):
        """We establish the direction """
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
        self.get_object(new_x, new_y)
        self.mac_out(new_x, new_y)
        self.level.map[self.pos_y][self.pos_x] = ' '
        self.pos_x = new_x
        self.pos_y = new_y
        self.level.map[self.pos_y][self.pos_x] = 'M'
        sound_mac_move = pygame.mixer.Sound(MAC_STEP)
        sound_mac_move.play()

    def get_object(self, x, y):
        """ The character gets an object """
        sound_mac_getobject = pygame.mixer.Sound(MAC_GETOBJECT)
        if self.level.map[y][x] in "E":
            self.items.append("E")
            sound_mac_getobject.play()
        elif self.level.map[y][x] in "T":
            self.items.append("T")
            sound_mac_getobject.play()
        elif self.level.map[y][x] in "N":
            self.items.append("N")
            sound_mac_getobject.play()

    def mac_out(self, x, y):
        """ McGyver gets out if he finds the exit"""
        if self.level.map[y][x] == "G":
            if len(self.items) >= 3:
                self.win = True
            else:
                sound_mac_killed = pygame.mixer.Sound(GUARDIAN_FIRE)
                sound_mac_killed.play()
                self.end_game = True

    def game_over(self, window):
        image_game_over = pygame.image.load(OUT_MAC).convert()
        window.blit(image_game_over, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_SPACE:
                self.finish_game = True
            elif event.type == KEYDOWN and event.key == K_RETURN:
                self.start_again = True




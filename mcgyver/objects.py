import random
from constants import *
import pygame


class Objects:

    def __init__(self, name, image, labyrinth):
        self.name = name
        self.level = labyrinth
        self.im = pygame.image.load(image).convert_alpha()
        self.obj_x, self.obj_y = self.rand_position()
        self.x = self.obj_x * sprite_size
        self.y = self.obj_y * sprite_size

    def rand_position(self):
        """ Randomly placing the objects """
        self.obj_y = random.randint(0, 14)
        self.obj_x = random.randint(0, 14)
        while self.level.map[self.obj_y][self.obj_x] != 'X':
            if self.level.map[self.obj_y][self.obj_x] == ' ':
                self.level.map[self.obj_y][self.obj_x] = self.name
                return self.obj_x, self.obj_y
            else:
                return self.rand_position()
        else:
            return self.rand_position()

    def display(self, window):
        window.blit(self.im, (self.x, self.y))

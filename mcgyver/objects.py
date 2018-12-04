import random
from constants import *
import pygame


class Objects:

    def __init__(self, name, image, labyrinth):
        self.name = name
        self.level = labyrinth
        self.im = pygame.image.load(image).convert_alpha()
        self.obj_x, self.obj_y = self.rand_position()
        self.x = self.obj_x * SPRITE_SIZE
        self.y = self.obj_y * SPRITE_SIZE

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

    def displaying_objects(self, level, screen):
        for line in level.map:
            for case in line:
                if self.name in case:
                    screen.blit(self.im, (self.obj_x * SPRITE_SIZE, self.obj_y * SPRITE_SIZE))
                """elif "T" in case:
                    screen.blit(tube.im, (tube.obj_x * SPRITE_SIZE, tube.obj_y * SPRITE_SIZE))
                elif "E" in case:
                    screen.blit(ether.im, (ether.obj_x * SPRITE_SIZE, ether.obj_y * SPRITE_SIZE))"""

    def display(self, window):
        window.blit(self.im, (self.x, self.y))

    def rank_in_list(self, character, window):
        if character.items[0] == self.name:
            window.blit(self.im, (193, 605))
        elif character.items[1] == self.name:
            window.blit(self.im, (257, 605))
        elif character.items[2] == self.name:
            window.blit(self.im, (323, 605))
        if len(character.items) >= 3:
                syringe = pygame.image.load(IMAGE_SYRINGE).convert()
                window.blit(syringe, (433, 605))

    def display_in_inventory(self, character, window):
        if self.name in character.items:
            self.rank_in_list(character, window)

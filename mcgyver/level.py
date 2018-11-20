from character import Character
from objects import Objects
from constants import *
import pygame


class Level:
    def __init__(self):
        self.file = "file_map.txt"
        self.map = self.map_generator()

    def map_generator(self):
        """ Loading map from file and put it into a double list """
        with open(self.file, 'r') as file:
            level_map = []
            for line in file:
                level_line = []
                for case in line:
                    if case != '\n':
                        level_line.append(case)
                level_map.append(level_line)
            return level_map
                
    def check_new_coors(self, x, y):
        if not 0 <= x <= 14 and not 0 <= y <= 14:
            return False
        if self.map[y][x] == 'X':
            return False
        return True

    '''def map_printer(self):
        """ Showing map like written in the .txt"""
        for line in self.map:
            for case in line:
                print(case, end=' ')
            print()'''

    def map_draw(self, screen):
        brick = pygame.image.load(image_brick)
        floor = pygame.image.load(image_floor)

        num_line = 0
        for line in self.map:
            num_case = 0
            for sprite in line:
                x = num_case * sprite_size
                y = num_line * sprite_size
                if sprite == 'X':
                    screen.blit(brick, (x, y))
                elif sprite == ' ':
                    screen.blit(floor, (x, y))
                num_case += 1
            num_line += 1

    @staticmethod
    def map_reset():
        """ Resetting the map before and after the game"""
        level = Level()
        level.map_generator()
        Objects('N', level)
        Objects('T', level)
        Objects('E', level)
        mcgyver = Character(0, 1, image_mcgyver, level)
        guardian = Character(13, 14, image_guardian, level)
        mcgyver.items = 0
        return level, mcgyver, guardian




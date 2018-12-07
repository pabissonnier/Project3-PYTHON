from constants import *
import pygame
from pygame.locals import *


class Level:
    """ Class used to obtain the maze """
    def __init__(self):
        self.file = "file_map.txt"
        self.map = self.map_generator()

    @staticmethod
    def player_decision():
        """ The player chooses to quit the game or to continue """
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE \
                    or event.type == KEYDOWN and event.key == K_SPACE:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_RETURN:
                return True

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
                
    def check_new_coors(self, next_x, next_y):
        """ Checks if new coordinates are possible, function used in character class """
        if not 0 <= next_x <= 14 or not 0 <= next_y <= 14:
            return False
        elif self.map[next_y][next_x] == 'X':
            return False
        return True

    def map_draw(self, screen):
        """ Used to draw the maze with graphic elements"""
        brick = pygame.image.load(IMAGE_BRICK).convert()
        num_line = 0
        for line in self.map:
            num_case = 0
            for sprite in line:
                x = num_case * SPRITE_SIZE
                y = num_line * SPRITE_SIZE
                if sprite == 'X':
                    screen.blit(brick, (x, y))
                num_case += 1
            num_line += 1






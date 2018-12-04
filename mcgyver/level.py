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
        if not 0 <= x <= 14 or not 0 <= y <= 14:
            return False
        elif self.map[y][x] == 'X':
            return False
        return True

    def map_draw(self, screen):
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






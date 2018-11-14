from character import Character
from objects import Objects


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

    def map_printer(self): # Print the map twice in each style
        """ Showing map like written in the .txt"""
        for line in self.map:
            for case in line:
                print(case, end=' ')
            print()

    @staticmethod
    def map_reset():
        """ Resetting the map before and after the game"""
        level = Level()
        level.map_generator()
        Objects('N', level)
        Objects('T', level)
        Objects('E', level)
        mcgyver = Character(0, 1, level)
        mcgyver.items = 0
        return level, mcgyver




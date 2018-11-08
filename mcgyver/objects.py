import random


class Objects:

    def __init__(self, name, labyrinth):
        self.name = name
        self.level = labyrinth
        self.obj_x, self.obj_y = self.rand_position()

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




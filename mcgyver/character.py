class Character:

    def __init__(self, ini_x, ini_y):
        self.pos_x = ini_x
        self.pos_y = ini_y

    def move(self, level):

        """We establish the direction """
        direction = input("Make McGyver move by using 'z', 's', 'w', or 'q' :")
        direction.lower()

        try:
            assert direction == 'z' or direction == 's' or direction == 'w' or direction == 'q'
        except AssertionError:
            print("Wrong value")

        """ Direction right """
        if direction == 's' and level.check_new_coors(level, self.pos_x + 1, self.pos_y):
            level[self.pos_y][self.pos_x] = ' '
            self.pos_x += 1
            level.level[self.pos_y][self.pos_x] = 'M'
            
        """ Direction up """
        if direction == 'z' and level.check_new_coors(level, self.pos_x, self.pos_y - 1):
            level[self.pos_y][self.pos_x] = ' '
            self.pos_y -= 1
            level[self.pos_y][self.pos_x] = 'M'
            
        """ Direction left """
        if direction == 'q' and level.check_new_coors(level, self.pos_x - 1, self.pos_y):
            level[self.pos_y][self.pos_x] = ' '
            self.pos_x -= 1
            level[self.pos_y][self.pos_x] = 'M'
            
        """ Direction down """
        if direction == 'w' and level.check_new_coors(level, self.pos_x, self.pos_y + 1):
            level[self.pos_y][self.pos_x] = ' '
            self.pos_y += 1
            level[self.pos_y][self.pos_x] = 'M'
                
        return level

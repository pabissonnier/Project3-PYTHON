
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
        if direction == 's' and self.pos_x < 14 and level[self.pos_y][self.pos_x + 1] != 'X':
            level.labyrinth[self.pos_y][self.pos_x] = ' '
            self.pos_x += 1
            level.labyrinth[self.pos_y][self.pos_x] = 'M'
            
        """ Direction up """
        if direction == 'z' and self.pos_y > 0 and level[self.pos_y - 1][self.pos_x] != 'X':
            level[self.pos_y][self.pos_x] = ' '
            self.pos_y -= 1
            level[self.pos_y][self.pos_x] = 'M'
            
        """ Direction left """
        if direction == 'q' and self.pos_x > 0 and level[self.pos_y][self.pos_x - 1] != 'X':
            level[self.pos_y][self.pos_x] = ' '
            self.pos_x -= 1
            level[self.pos_y][self.pos_x] = 'M'
            
        """ Direction down """
        if direction == 'w' and self.pos_y < 14 and level[self.pos_y + 1][self.pos_x] != 'X':
            level[self.pos_y][self.pos_x] = ' '
            self.pos_x += 1
            level[self.pos_y][self.pos_x] = 'M'
                
        print(level)

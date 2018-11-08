from objects import Objects


class Character:

    def __init__(self, ini_x, ini_y, labyrinth):
        self.pos_x = ini_x
        self.pos_y = ini_y
        self.level = labyrinth
        self.items = []

    def move(self):

        """We establish the direction """
        direction = input("Make McGyver move by using 'z', 's', 'w', or 'q' :")
        direction.lower()

        try:
            assert direction == 'z' or direction == 's' or direction == 'w' or direction == 'q'
        except AssertionError:
            print("Wrong value")

        """ Direction right """
        if direction == 's' and self.level.check_new_coors(self.pos_x + 1, self.pos_y):
            self.level.map[self.pos_y][self.pos_x] = ' '
            self.pos_x += 1
            self.level.map[self.pos_y][self.pos_x] = 'M'

        """ Direction up """
        if direction == 'z' and self.level.check_new_coors(self.pos_x, self.pos_y - 1):
            self.level.map[self.pos_y][self.pos_x] = ' '
            self.pos_y -= 1
            self.level.map[self.pos_y][self.pos_x] = 'M'

        """ Direction left """
        if direction == 'q' and self.level.check_new_coors(self.pos_x - 1, self.pos_y):
            self.level.map[self.pos_y][self.pos_x] = ' '
            self.pos_x -= 1
            self.level.map[self.pos_y][self.pos_x] = 'M'

        """ Direction down """
        if direction == 'w' and self.level.check_new_coors(self.pos_x, self.pos_y + 1):
            self.level.map[self.pos_y][self.pos_x] = ' '
            self.pos_y += 1
            self.level.map[self.pos_y][self.pos_x] = 'M'

        return self.level.map

    def mac_out(self):
        """ McGyver gets out if he find the exit"""
        if self.pos_y == 13 and self.pos_x == 14:
            print("WELL DONE !! You got out !")
            answer = input("Do you want to play again ? y/n ")
            answer.lower()
            if answer == 'y':
                return True
            elif answer == 'n':
                return False
            else:
                print("Wrong answer")

    def get_object(self):
        """ The character gets an object """
        # If mcgyver position is equal to object position:
        # The objects is put in the inventory
        pass


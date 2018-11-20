import pygame
from pygame.locals import *
from constants import *


class Character:

    def __init__(self, ini_x, ini_y, image, labyrinth):
        self.pos_x = ini_x
        self.pos_y = ini_y
        self.level = labyrinth
        self.image = pygame.image.load(image).convert_alpha()
        self.items = 0
        self.end_game = False
        self.win = False

    def move(self):
        """We establish the direction """

        """direction = input("Make McGyver move by using 'z', 's', 'w', or 'q' :")
        direction.lower()"""
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_s and self.level.check_new_coors(self.pos_x + 1, self.pos_y):
                    self.do_move((self.pos_x + 1) * sprite_size, self.pos_y)
                elif event.key == K_z and self.level.check_new_coors(self.pos_x, self.pos_y - 1):
                    self.do_move(self.pos_x, (self.pos_y - 1) * sprite_size)
                elif event.key == K_q and self.level.check_new_coors((self.pos_x - 1) * sprite_size, self.pos_y):
                    self.do_move(self.pos_x - 1, self.pos_y)
                elif event.key == K_w and self.level.check_new_coors(self.pos_x, (self.pos_y + 1) * sprite_size):
                    self.do_move(self.pos_x, self.pos_y + 1)
                else:
                    pass

    def do_move(self, new_x, new_y):
        self.get_object(new_x, new_y)
        self.mac_out(new_x, new_y)
        self.level.map[self.pos_y][self.pos_x] = ' '
        self.pos_x = new_x
        self.pos_y = new_y
        self.level.map[self.pos_y][self.pos_x] = 'M'

    def get_object(self, x, y):
        """ The character gets an object """
        if self.level.map[y][x] in ["E", "N", "T"]:
            self.items += 1
            print("Your inventory contains", self.items, " objects.")

    def mac_out(self, x, y):
        """ McGyver gets out if he finds the exit"""
        if self.level.map[y][x] == "G":
            if self.items >= 3:
                print("Thanks to your 3 items, you have made a syringe to asleep the guardian !")
                print("WELL DONE !! You got out !")
                self.win = True
                self.game_over()
            else:
                print("You need to find the 3 objects to get out !!")

    def game_over(self):
        answer = str(input("Do you want to play again ? y/n "))
        answer.lower()
        if answer == 'y':
            self.end_game = False
        elif answer == 'n':
            self.end_game = True
        else:
            print(" Wrong answer")
            self.game_over()



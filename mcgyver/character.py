import pygame
from constants import *


class Character:

    def __init__(self, ini_x, ini_y, image, labyrinth):
        self.pos_x = ini_x
        self.pos_y = ini_y
        self.x = self.pos_x * sprite_size
        self.y = self.pos_y * sprite_size
        self.level = labyrinth
        self.items = []
        self.visual = pygame.image.load(image).convert_alpha()
        self.end_game = False

    def display(self, window):
        window.blit(self.visual, (self.x, self.y))

    def move(self, direction):
        """We establish the direction """
        if direction == "right" and self.level.check_new_coors(self.pos_x + 1, self.pos_y):
            self.do_move(self.pos_x + 1, self.pos_y)
        elif direction == "up" and self.level.check_new_coors(self.pos_x, self.pos_y - 1):
            self.do_move(self.pos_x, self.pos_y - 1)
        elif direction == "left" and self.level.check_new_coors(self.pos_x - 1, self.pos_y):
            self.do_move(self.pos_x - 1, self.pos_y)
        elif direction == "down" and self.level.check_new_coors(self.pos_x, self.pos_y + 1):
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
        if self.level.map[y][x] in "E":
            self.items.append("E")
        if self.level.map[y][x] in "T":
            self.items.append("T")
        if self.level.map[y][x] in "N":
            self.items.append("N")

        print(self.items)
        """if self.level.map[y][x] in ["E", "N", "T"]:
            self.items += 1
            print("Your inventory contains", self.items, " objects.")"""

    def mac_out(self, x, y):
        """ McGyver gets out if he finds the exit"""
        if self.level.map[y][x] == "G":
            if len(self.items) >= 3:
                print("You have made a syringe to asleep the guardian")
                print("Well done !! You are free !!")
                self.game_over()
                return True
            else:
                return False

    def game_over(self):
        answer = str(input("Do you want to play again? y or n :"))
        answer.lower()
        if answer == 'y':
            self.end_game = False
        elif answer == 'n':
            self.end_game = True
        else:
            print(" Wrong answer")
            self.game_over()



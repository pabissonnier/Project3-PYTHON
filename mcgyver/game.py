#! /usr/bin/env python3
# coding: utf-8

from level import Level


def main():
    print("Welcome !")
    print("Help McGyver to escape the labyrinth !")
    print("Grab the 3 objects and find the exit to beat the guardian...")

    """ Creation of the labyrinth"""
    level = Level()
    level.map_generator("file_map.txt")







if __name__ == "__main__":
    main()

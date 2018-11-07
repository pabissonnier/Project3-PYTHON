class Level:
    def __init__(self):
        self.labyrinth = None

    def map_generator(self, file_to_open):
        """ Loading map from file and put it into a double list """
        with open(file_to_open, 'r') as file:
            level = []
            for line in file:
                level_line = []
                for case in line:
                    if case != '\n':
                        level_line.append(case)
                level.append(level_line)
                
    def check_new_coors(self, labyrinth, x, y):
        if not 0 <= x <= 14 and not 0 <= y <= 14:
            return False
        if labyrinth[y][x] == 'X':
            return False
        return True





"""def map_printer(self, level):
    #Showing map like written in the .txt
    for i in range(level[x]):

    show_map_lines = "".join(level)
    show_map = "\n".join(show_map_lines)
    print(show_map)"""


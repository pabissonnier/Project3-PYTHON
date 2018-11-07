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





"""def map_printer(self, level):
    #Showing map like written in the .txt
    for i in range(level[x]):

    show_map_lines = "".join(level)
    show_map = "\n".join(show_map_lines)
    print(show_map)"""


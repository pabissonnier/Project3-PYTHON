class Level:
    def __init__(self):
        self.labyrinth = None

    def map_generator(self, file_to_open):
        """ Loading map from file and put it into a double list """
        with open(file_to_open, 'r') as file:
            labyrinth = []
            for line in file:
                laby_line = []
                for case in line:
                    if case != '\n':
                        laby_line.append(case)
                labyrinth.append(laby_line)
                

    

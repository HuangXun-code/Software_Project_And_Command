import random

class Model(object):
    
    def __init__(self, num_of_rows=50, num_of_cols=50, ratio=0.1):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.round = 0
        self.map = list()
        self.map = [[1 if random.random() < ratio else 0 \
                     for j in range(num_of_cols)] for i in range(num_of_cols)]
    
    def update(self):
        backup = list()
        backup = [[self.map[i][j] for j in range(self.num_of_cols)] for i in range(self.num_of_rows)]
        for i in range(self.num_of_rows):
            for j in range(self.num_of_cols):
                if self.count_neighbours(i, j, backup) == 3:
                    self.map[i][j] = 1
                elif self.count_neighbours(i, j, backup) != 2:
                    self.map[i][j] = 0
        self.round += 1
    
    def count_neighbours(self, i, j, backup):
        up = i - 1 if i > 0 else self.num_of_rows - 1
        down = i + 1 if i < self.num_of_rows - 1 else 0
        left = j - 1 if j > 0 else self.num_of_cols - 1
        right = j + 1 if j < self.num_of_cols - 1 else 0
        return backup[i][left] + backup[i][right] + backup[up][j] + backup[down][j] + backup[up][left] \
               + backup[up][right]+ backup[down][left] + backup[down][right]

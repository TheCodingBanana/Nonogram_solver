import numpy as np


class NonogramGame:
    def __init__(self, conditions):
        self.conditions = conditions
        self.size = (len(conditions[0]), len(conditions[1]))
        self.column_conditions = conditions[1] 
        self.row_conditions = conditions[0]
        self.board = np.zeros(self.size)
        self.completed_rows = np.zeros(self.size[0])
        self.completed_columns = np.zeros(self.size[1])
    
    
    def complete_rows_columns(self):
        for i in range(self.size[0]): # Rows
            twos_total = list(self.board[i, :]).count(2)
            ones_total = list(self.board[i, :]).count(1)
            combined_total = twos_total + ones_total
            if combined_total == self.size[1]:
                self.completed_rows[i] = 1
            elif twos_total == sum(self.row_conditions[i]):
                for j in range(self.size[1]):
                    if self.board[i, j] == 0:
                        self.board[i, j] = 1
                self.completed_rows[i] = 1

        for i in range(self.size[1]): #Columns
            twos_total = list(self.board[:, i]).count(2)
            ones_total = list(self.board[:, i]).count(1)
            combined_total = twos_total + ones_total
            if combined_total == self.size[0]:
                self.completed_columns[i] = 1
            elif twos_total == sum(self.column_conditions[i]):
                for j in range(self.size[0]):
                    if self.board[j, i] == 0:
                        self.board[j, i] = 1
                self.completed_columns[i] = 1
    
    def solve_first_last_LS(self):
        for i in range(self.size[0]): #Rows
            if self.completed_rows[i] == 1:
                continue
            zeros = [j for j, x in enumerate(list(self.board[i, :])) if x == 0]
            twos = [j for j, x in enumerate(list(self.board[i, :])) if x == 2]
            print(zeros)
            
            print(twos)



    def solve_nonogram(self):
        for row_nr, row_condition in enumerate(self.row_conditions): # First pass Rows
            reduced_row = []
            counter = 0
            for i, line_segment in enumerate(row_condition):
                counter += 1
                reduced_row = reduced_row + list(np.ones(line_segment)*counter)
                if i != len(row_condition)-1:
                    counter += 1
                    reduced_row = reduced_row + [counter]
            v1_row = reduced_row.copy()
            v2_row = reduced_row.copy()
            while len(v1_row) < self.size[1]:
                v1_row.append(0)
                v2_row.insert(0, 0)
            for index, (b1, b2) in enumerate(zip(v1_row, v2_row)):
                if b1 == b2 and b1 != 0:
                    if b1%2 == 0:
                        value = 1
                    else:
                        value = 2
                    self.board[row_nr][index] = value
        for column_nr, column_condition in enumerate(self.column_conditions):# First pass Columns
            reduced_column  = []
            counter = 0
            for i, line_segment in enumerate(column_condition):
                counter += 1
                reduced_column = reduced_column + list(np.ones(line_segment)*counter)
                if i != len(column_condition)-1:
                    counter += 1
                    reduced_column = reduced_column + [counter]
            v1_column = reduced_column.copy()
            v2_column = reduced_column.copy()
            while len(v1_column) < self.size[0]:
                v1_column.append(0)
                v2_column.insert(0, 0)
            for index, (b1, b2) in enumerate(zip(v1_column, v2_column)):
                if b1 == b2 and b1 != 0:
                    if b1%2 == 0:
                        value = 1
                    else:
                        value = 2
                    self.board[index][column_nr] = value    

        #Check for completed columns/rows:
        self.complete_rows_columns()
        self.solve_first_last_LS()
        #print(self.board)



example_conditions = ([[1], [2], [2, 1], [1, 1]], [[2],  [2], [2, 1], [1]])
example_nonogram2 = NonogramGame(example_conditions)
example_nonogram2.solve_nonogram()
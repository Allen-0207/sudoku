import copy
import random

'''
Use backtracking algorithm create 
'''

class Game:
    def __init__(self, code = None):
        self.solved_board = []
        self.board = []
        self.sudoku_matrix = []
        self.sudoku_solved = []
        self.counter = 0
        self.__resetBoard()

    
    def __resetBoard(self):
        self.solved_board = [[0 for i in range(9)] for j in range(9)]
        self.board = [[0 for i in range(9)] for j in range(9)]

    def generate_board(self, level = 1):
        self.__resetBoard()
        self.generate(0, 0)
        # print(self.solved_board)

        remove_cell = 32
        
        if(level == 1):
            remove_cell = random.randint(32, 38)
        elif(level == 2):
            remove_cell = random.randint(40, 46)
        elif(level == 3):
            remove_cell = random.randint(48, 52)
        elif(level == 4):
            remove_cell = random.randint(54, 56)
        elif(level == 5):
            remove_cell = random.randint(59, 61)
        
        self.board = copy.deepcopy(self.solved_board)

        index = [i for i in range(81)]

        while(remove_cell > 0):
            cell_id = random.sample(index, 1)[0]
            row = cell_id // 9
            col = cell_id % 9

            index.remove(cell_id)
            
            back_up_val = self.board[row][col]
            self.board[row][col] = 0

            self.solution_count()
            if(self.counter > 1):
                self.board[row][col] = back_up_val
            else:
                remove_cell -= 1
            self.counter = 0
        
        # print(self.board)
        return self.board
    
    # backtracking 
    def generate(self, i, j):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if(j > 8):
            j = 0
            i += 1

            if i > 8:
                return True
        
        #skip cell
        if(self.solved_board[i][j] != 0):
            if(self.generate(i, j + 1)):
                return True
        else:
            random.shuffle(number_list)
            for val in number_list:
                if self.validate_cell(self.solved_board, val, i, j):
                    self.solved_board[i][j] = val
                    if(self.generate(i, j + 1)):
                        return True
                    self.solved_board[i][j] = 0
        return False
    
    def validate_cell(self, board, val, i, j):
        block_i = i // 3
        block_j = j // 3

        # Check block
        for b_i in range(block_i * 3, block_i * 3 + 3):
            for b_j in range(block_j * 3, block_j * 3 + 3):
                if(self.board[b_i][b_j] == val):
                    return False

        # Check row
        for col in range(0, 9):
            if(self.board[i][col] == val):
                return False
        
        # Check column
        for row in range(0, 9):
            if(self.board[row][j] == val):
                return False

        return True        
    

    def solution_count(self):
        self.sudoku_matrix = copy.deepcopy(self.board)
        self.sudoku_solved =  copy.deepcopy(self.board)
        self.__count_solutions__(0, 0)

    def __count_solutions__(self, i, j):
        if j > 8:
            j = 0
            i += 1
            if(i > 8):
                self.counter += 1
                return
            
            if(self.sudoku_solved[i][j] != 0):
                self.__count_solutions__(i, j + 1)
            else:
                for val in range(1, 9):
                    if(self.validate_cell(self.sudoku_solved, val, i, j)):
                        self.sudoku_solved[i][j] = val
                        self.__count_solutions__(i, j + 1)
                        self.sudoku_solved[i][j] = 0
                        if(self.counter > 1):
                            return
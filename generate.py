import copy
import random

'''
Use backtracking algorithm create 
'''

class Board:
    def __init__(self, code = None):
        self.__resetBoard()

        if(code):
            self.code = code

            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(code[0])
                    code = code[1:]
        else:
            self.code = None

    
    def __resetBoard(self):
        self.board = [[0 for i in range(9)] for j in range(9)]

    def generate_board(self):
        self.__resetBoard()
        

        self.generate(0, 0)
        print(self.board)
    
    def generate(self, i, j):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if(j > 8):
            j = 0
            i += 1

            if i > 8:
                return True
        
        #skip cell
        if(self.board[i][j] != 0):
            if(self.generate(i, j + 1)):
                return True
        else:
            random.shuffle(number_list)
            for val in number_list:
                if self.validate_cell(val, i, j):
                    self.board[i][j] = val
                    if(self.generate(i, j + 1)):
                        return True
                    self.board[i][j] = 0
        return False
    
    def validate_cell(self, val, i, j):
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
    
''' 
- Display the game stage 



'''
import numpy as np

class Stage : 
    # init 
    def __init__(self, board: np.array) : 
        self.board = board
        for i in range(self.board.shape[0]) : 
            for j in range(self.board.shape[1]) : 
                if self.board[i, j] == 0 : 
                    self.zero_poss = (i,  j)

    # check winning stage 
    def is_Win(self) : 
        for i in range(self.board.shape[0]) : 
            for j in range(self.board.shape[1]) : 
                if  self.board[i, j] != i * self.board.shape[0] + j : return False 

        return True 
    
    # change stage
    # dir = 0 : right , dir = 1 : left, dir = 2 : up, dir = 3 : down 
    def change(self, dir :int) : 
        z_i = self.zero_poss[0]
        z_j = self.zero_poss[1]
    
        if dir == 0 and z_j + 1 < self.board.shape[1] : 
            self.board[z_i, z_j], self.board[z_i, z_j + 1] = self.board[z_i, z_j + 1], self.board[z_i, z_j]
            
        if dir == 1 and z_j - 1 >= 0 : 
            self.board[z_i, z_j], self.board[z_i, z_j - 1] = self.board[z_i, z_j - 1], self.board[z_i, z_j]

        if dir == 2 and z_i - 1 >= 0 : 
            self.board[z_i, z_j], self.board[z_i - 1, z_j] = self.board[z_i - 1, z_j ], self.board[z_i, z_j] 

        if dir == 3 and z_i + 1 < self.board.shape[0] : 
            self.board[z_i, z_j], self.board[z_i + 1, z_j] = self.board[z_i + 1, z_j], self.board[z_i, z_j]

        return self.board


        



    
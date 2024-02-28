''' 
- Display the game stage 
'''
import numpy as np



class Node : 

    # init 
    def __init__(self, board: np.array, zero_poss: tuple) : 
        self.board = board
        self.zero_poss = zero_poss
        self.previous_stage = None

    # check winning stage 
    def is_Win(self) : 
        for i in range(self.board.shape[0]) : 
            for j in range(self.board.shape[1]) : 
                if  self.board[i, j] != i * self.board.shape[0] + j : return False 

        return True 
    
    # this function connect to search algorithm module to find solution 
    def solve(self, search_algo: str) : 
        pass


        



    
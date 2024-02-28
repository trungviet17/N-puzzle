''' 
- Display the game stage 
'''
import numpy as np
from  heuristic_function import Heuristic



class Node : 

    # init 
    def __init__(self, board: np.array, zero_poss: tuple,  previous_stage: tuple, is_manhattan: bool) : 
        self.board = board
        self.zero_poss = zero_poss
        self.previous_stage = previous_stage
        self.is_man = is_manhattan
        if is_manhattan :
            self.h_value = Heuristic.manhattan_distance(board)
        else : 
            self.h_value = Heuristic.the_number_of_misstitle(board)

    # check winning stage 
    def is_Win(self) : 
        for i in range(self.board.shape[0]) : 
            for j in range(self.board.shape[1]) : 
                if  self.board[i, j] != i * self.board.shape[0] + j : return False 

        return True 
    
    def __lt__(self, other): 
        return other.h_value > self.h_value
         
     
    


        



    
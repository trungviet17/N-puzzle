import numpy as np
from copy import deepcopy 

'''
- Change direction of game stage
'''

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTION = [UP, DOWN, LEFT, RIGHT]
class Move:

    def move(self, stage: np.array, swap: tuple, zeros_pos = (-1, -1)):
        if zeros_pos == (-1, -1): 
            zeros_pos = self.find_poss(stage, 0)

        x = zeros_pos[0] + swap[0]
        y = zeros_pos[1] + swap[1]

        if (x < stage.shape[0] and y < stage.shape[1] and min(x, y) >= 0) : 
            new_stage = deepcopy(stage)
            new_stage[zeros_pos[0], zeros_pos[1]], new_stage[x, y] = new_stage[x, y], new_stage[zeros_pos[0], zeros_pos[1]]
            return new_stage
        
        return None


    def find_poss(self, stage: np.array, num: int): 
        for i in range(stage.shape[0]): 
            for j in range(stage.shape[1]): 
                if stage[i, j] == num : return (i, j)
        return (None, None)
    

    def up(self,stage): 
        return self.move(stage, UP)
    
    def down(self, stage): 
        return  self.move(stage, DOWN)
    
    def left(self, stage): 
        return self.move(stage, LEFT)
    def right(self, stage): 
        return self.move(stage,  RIGHT)
'''
- This module use to calculate heuristic variable in 3 method : 
    - Using manhattan method 
    - Using number_of_misstitle 
'''
import numpy as np
class Heuristic: 

    def the_number_of_misstitle( board: np.array): 
        res = 0 

        for i in range(board.shape[0]) :
            for j in range(board.shape[1]): 
                if board[i, j] != i * board.shape[0] + j : res += 1 

        return res


    def manhattan_distance( board): 
        res = 0 

        for i in range(board.shape[0]): 
            for j in range(board.shape[1]): 
                x_true = int(board[i,j] // board.shape[0])
                y_true = int(board[i, j] % board.shape[0])

                res += abs(i - x_true) + abs(j - y_true)
        return res

    
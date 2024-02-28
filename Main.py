'''
-   This file is used like a interface for user to interact with game
-   Display stage of game

'''
from Node import Node 
from Search_Algorithm import Search_Algorithm
from move import move, find_poss
import numpy as np 

board = np.random.permutation(9).reshape((3, 3))
print(board)
zero_poss = find_poss(board, 0)
first_Node = Node(board= board, zero_poss= zero_poss, previous_stage= (-1, -1), is_manhattan= True )

step, _ = Search_Algorithm(first_Node).greedysearch(True)

print(step)
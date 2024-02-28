'''
- Implement uniform search algorithm : 
    - BFS 
    - DFS 
    - UCS 

- Direction encode : dir = 0 : right , dir = 1 : left, dir = 2 : up, dir = 3 : down 
'''
from Node import Node
import numpy as np
from collections import deque, defaultdict



class Search_Algorithm : 
    def __init__(self, stage :Node) :
        self.stage = stage
        # store postition that 0 change to win
        self.tracking = defaultdict(int)

    # BFS 
    def bfs(self, limit :int ) : 
        q = deque()
        q.append(self.stage)

        while q and limit : 
            front = q.popleft()

            if front.is_Win() : break

            pass

        pass

    # DFS 
    def dfs(self) : 
        

        pass 


    def ucs(self) : 


        pass




    def greedysearch(self): 
        pass

    
    def a_star(self): 
        pass

    
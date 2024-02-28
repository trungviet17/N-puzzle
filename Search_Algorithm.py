'''
- Implement uniform search algorithm : 
    - BFS 
    - Greedy Search


'''
from Node import Node
import numpy as np
from collections import deque
from move import UP, LEFT, RIGHT, DOWN, DIRECTION, move
import heapq


class Search_Algorithm : 
    def __init__(self, stage :Node) :
        self.stage = stage
        
    # BFS 
    def bfs(self) : 
        q = deque()
        q.append(self.stage)
        res = 0 
        while q : 
            sz = len(q) 
            for _ in range(sz) : 
                front = q.popleft()
                if front.is_Win() : return (res, front)
                for i in range(4) : 
                    dir = DIRECTION[i]

                    sub = move(stage= front.board, swap = dir, zeros_pos= front.zero_poss)
                    if sub is None : continue 

                    new_node = Node(sub, (front.zero_poss[0] + dir[0], front.zero_poss[1] + dir[1]), previous_stage= dir, is_manhattan= True)

                    q.append(new_node)
                res += 1

        return (None, None)

    # greedy search algorithm
    def greedysearch(self, is_manhattan = True): 
        q = [self.stage]
        
        res = 0 
        while q : 
            sz = len(q) 

            for _ in range(sz): 
                front = heapq.heappop(q)

                if front.is_Win() : return (res, front)

                for i in range(4) : 
                    dir = DIRECTION[i]

                    sub = move(stage = front.board, swap = dir, zeros_pos= front.zero_poss)
                    if sub is None : continue 

                    new_node = Node(sub, (front.zero_poss[0] + dir[0], front.zero_poss[1] + dir[1]), previous_stage= dir, is_manhattan =is_manhattan )

                    q.append(new_node)
            res += 1 

        return (None, None)


        pass
        

    # DFS 
    def dfs(self) : 
        

        pass 


    def ucs(self) : 


        pass




    
    def a_star(self): 
        pass

    
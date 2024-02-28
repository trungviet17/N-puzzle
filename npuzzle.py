import numpy as np 
from collections import deque
import heapq


def bfs(board: np.array, zero_poss: tuple) : 
    q = deque()
    q.append((board, zero_poss))
    res = 0 

    while q : 
        sz = len(q)
        for k in range(sz) : 
            front = q.popleft()
            f_board = front[0]
            f_pos = front[1]
            if is_Win(front[0]) : return res 

            for dir in range(4) : 
                new_stage = change(f_board, f_pos, dir )
                if new_stage == None : continue 
                q.append(new_stage)

        res += 1 

    return -1 


def greedy_search(board: np.array, zero_poss: tuple): 
    first_score = greedy_score(board)

    board_info = [(board, zero_poss)]
    pq = []
    
    heapq.heappush(pq, (first_score,0))

    res = 0 
    while pq : 
        sz = len(pq)

        for z in range(sz): 
            front = heapq.heappop(pq)
            front_info = board_info[front[1]]
            front_score = front[0]

            if is_Win(front_info[0]) : return res 

            for d in range(4) : 
                new_stage, score_change = change(front_info[0], front_info[1], d)
                if new_stage == None : continue 

                new_score = front_score - score_change
                board_info.append(new_stage)
                heapq.heappush(pq, (new_score, len(board_info) - 1))
        res += 1 

    return res



def greedy_score(board: np.array) : 

    res = 0 
    for i in range(board.shape[0]) : 
            for j in range(board.shape[1]) : 
                if  board[i, j] != i * board.shape[0] + j : res += 1 
    return res



def change(bo: np.array, zero_poss: tuple, dir: int) : 
    z_i = zero_poss[0]
    z_j = zero_poss[1]
    board = np.copy(bo)
    score_change = 0
    # dir = 0 : right , dir = 1 : left, dir = 2 : up, dir = 3 : down

    if dir == 0 and z_j + 1 < board.shape[1] : 
        board[z_i, z_j], board[z_i, z_j + 1] = board[z_i, z_j + 1], board[z_i, z_j]
        if board[z_i, z_j] == z_i * board.shape[0] + j : score_change = 1 
        return (board, (z_i,  z_j + 1)) , score_change

    if dir == 1 and z_j -1  >= 0 : 
        board[z_i, z_j], board[z_i, z_j - 1] = board[z_i, z_j -1], board[z_i, z_j]
        if board[z_i, z_j] == z_i * board.shape[0] + j : score_change = 1
        return (board, (z_i, z_j - 1)) , score_change

    if dir == 2 and z_i -1 >= 0: 
        board[z_i, z_j], board[z_i - 1, z_j] = board[z_i - 1, z_j], board[z_i, z_j]
        if board[z_i, z_j] == z_i * board.shape[0] + j : score_change = 1
        return  (board, (z_i - 1, z_j)) , score_change
        
    if dir == 3 and z_i + 1 < board.shape[0]: 
        board[z_i, z_j], board[z_i + 1, z_j] = board[z_i + 1, z_j], board[z_i, z_j]
        if board[z_i, z_j] == z_i * board.shape[0] + j : score_change = 1
        return (board, (z_i + 1, z_j)), score_change

    return None, 0



def is_Win(board: np.array) : 
    for i in range(board.shape[0]) : 
            for j in range(board.shape[1]) : 
                if  board[i, j] != i * board.shape[0] + j : return False 

    return True 



if __name__ == '__main__' : 
    board = np.random.permutation(9).reshape((3, 3))
    poss_zero = (-1, -1)
    for i in range(3) : 
        for j in range(3) : 
            if board[i, j] == 0 : poss_zero = (i,j)
    print(board)

    board_1 = np.array([
        [1, 0, 2], [3, 4, 5], [6, 7, 8]
    ])

    print(greedy_search(board= board_1, zero_poss= (0, 1)))
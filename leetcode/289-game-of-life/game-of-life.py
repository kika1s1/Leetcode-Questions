from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        R, C = len(board), len(board[0])
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        
        def countLiveNeighbors(r, c):
            cnt = 0
            for x, y in directions:
                a, b = r + x, c + y
                if 0 <= a < R and 0 <= b < C and abs(board[a][b]) == 1:
                    cnt += 1
            return cnt
        
        for i in range(R):
            for j in range(C):
                live_neighbors = countLiveNeighbors(i, j)
                
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2  
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1

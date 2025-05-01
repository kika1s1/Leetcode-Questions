class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRECTIONS = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        maxim = 0
        cache = [[0] * COLS for _ in range(ROWS)]  
        def inbound(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS
        
        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]  
            length = 1  
            for r, c in DIRECTIONS:
                new_row = i + r
                new_col = j + c
                if inbound(new_row, new_col) and matrix[new_row][new_col] > matrix[i][j]:
                    length = max(length, 1 + dfs(new_row, new_col))  
                    
            cache[i][j] = length  
            return length
        
        for i in range(ROWS):
            for j in range(COLS):
                maxim = max(maxim, dfs(i, j))
        
        return maxim
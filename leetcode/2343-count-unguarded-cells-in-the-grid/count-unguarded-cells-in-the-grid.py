from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid
        grid = [[False for _ in range(n)] for _ in range(m)]
        
        # Place guards and walls
        for i, j in guards:
            grid[i][j] = "G"
        for i, j in walls:
            grid[i][j] = "W"
        
        # Helper function to check if a cell is within bounds
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        
        # Mark guarded cells
        for i, j in guards:
            # Left
            c = j - 1
            while inbound(i, c) and grid[i][c] != "W" and grid[i][c] != "G":
                grid[i][c] = True
                c -= 1
            # Right
            c = j + 1
            while inbound(i, c) and grid[i][c] != "W" and grid[i][c] != "G":
                grid[i][c] = True
                c += 1
            # Up
            r = i - 1
            while inbound(r, j) and grid[r][j] != "W" and grid[r][j] != "G":
                grid[r][j] = True
                r -= 1
            # Down
            r = i + 1
            while inbound(r, j) and grid[r][j] != "W" and grid[r][j] != "G":
                grid[r][j] = True
                r += 1

        # Count unguarded cells
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == False:
                    cnt += 1
        
        return cnt

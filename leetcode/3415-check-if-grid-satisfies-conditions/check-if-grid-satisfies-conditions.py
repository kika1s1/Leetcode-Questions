from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS-1):
            for j in range(COLS-1):
                if grid[i][j] !=grid[i+1][j]:
                    return False
                if grid[i][j] == grid[i][j+1]:
                    return False
                if grid[i+1][j] ==grid[i+1][j+1]:
                    return False
            if grid[i][0] != grid[i+1][0]:
                return False
        for i in range(COLS-1):
            if grid[0][i] == grid[0][i+1]:
                return False
        return True
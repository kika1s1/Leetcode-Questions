# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxim  = 0
        visited = set() 
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c)) 
            fish_value = grid[r][c]
            
            total_fish = fish_value + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
            # visited.remove((r, c))  
            return total_fish
        
        for i in range(ROWS):
            for j in range(COLS):
                maxim = max(dfs(i, j), maxim)
        
        return maxim
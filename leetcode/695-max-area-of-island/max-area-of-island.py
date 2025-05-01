class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(grid), len(grid[0])
        def inbound(r, c):
            return 0 <= r < R and 0 <=c < C
        def dfs(i, j):
            grid[i][j] = 0
            count = 1  
            for x, y in direction:
                nr, nc = x + i, y + j
                if inbound(nr, nc) and grid[nr][nc] == 1:
                    count += dfs(nr, nc)
            return count
        maxim = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    maxim = max(maxim, dfs(i,j))
        return maxim

        

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        def in_bound(r, c):
            return 0 <= r < R and 0 <= c < C
        cnt = 0
        visited = set()
        direction  = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            visited.add((i, j))
            for r, c in direction:
                nr, nc = i + r , c + j
                if in_bound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == "1":
                    dfs(nr, nc)
        ans = 0
        for i in range(R):
            for j in range(C):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    ans +=1
        return ans
                    
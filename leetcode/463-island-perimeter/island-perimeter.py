class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(grid), len(grid[0])
        def inbound(r, c):
            return 0 <=r <R and 0 <=c<C
        def perimeter(i, j, grid, visited):
            cnt = 0
            for x, y in directions:
                nr, nc = x + i, y + j
                if inbound(nr, nc) and grid[nr][nc] == 1:
                    cnt +=1
            return 4 - cnt

        ans  = 0
        visited = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans +=perimeter(i, j, grid, visited)
                visited.add((i, j))
        return ans

        
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        matrix = [[0 for i in range(C)]for i in range(R)]
        direction = [(-1, 1), (0, 1), (1, 1)]
        def inbound(r, c):
            return 0 <=r < R and 0 <=c < C
        for j in range(C-1):
            for i in range(R):
                if j == 0:
                    for x, y in direction:
                        nr, nc = i+x, j+y
                        if inbound(nr, nc):
                            if grid[i][j] < grid[nr][nc]:
                                matrix[nr][nc] = max(matrix[i][j] + 1, matrix[nr][nc])
                else:
                    if matrix[i][j] !=0:
                        for x, y in direction:
                            nr, nc = i+x, j+y
                            if inbound(nr, nc):
                                if grid[i][j] < grid[nr][nc]:
                                    matrix[nr][nc] = max(matrix[i][j] + 1, matrix[nr][nc])
        maxim = float("-inf")
        for row in matrix:
            maxim = max(maxim, max(row))                                
        return maxim
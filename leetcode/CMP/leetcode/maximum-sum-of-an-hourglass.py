class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def sum_hourglass(i, j):
            return sum(grid[i-1][j-1:j+2]) + grid[i][j] + sum(grid[i+1][j-1:j+2])
        rows = len(grid)
        cols = len(grid[0])
        best_sum = 0
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                best_sum = max(best_sum,sum_hourglass(i,j))
        return best_sum
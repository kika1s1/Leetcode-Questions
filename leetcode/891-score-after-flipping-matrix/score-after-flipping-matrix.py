class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        COLS, ROWS = len(grid[0]), len(grid)

        total = ROWS * (1 << (COLS - 1))
        for j in range(1, COLS):
            ones = sum(grid[i][j] == grid[i][0] for i in range(ROWS))
            flips = max(ones, ROWS - ones)
            total += flips * (1 << (COLS - 1 - j)) 
        return total
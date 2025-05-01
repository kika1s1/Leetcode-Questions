class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sum_top = sum(grid[0]) - grid[0][0]
        sum_bottom = 0
        res = max(sum_top, sum_bottom)

        for partition in range(1,len(grid[0])):
            sum_top -= grid[0][partition]
            sum_bottom += grid[1][partition-1]
            res = min(res, max(sum_top, sum_bottom))
        return res
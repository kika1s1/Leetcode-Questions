class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def helper(i):
            first, second, idx = inf, inf, None
            for j, val in enumerate(grid[i]):
                if val < first:
                    second = first
                    first = val
                    idx = j
                elif val < second:
                    second = val
            return (first, second, idx)
        
        for i in range(n-2, -1, -1):
            first, second, idx = helper(i+1)
            for j in range(n):
                if j != idx:
                    grid[i][j] += first
                else:
                    grid[i][j] += second
        return min(grid[0])
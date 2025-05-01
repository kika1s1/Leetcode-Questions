class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        
        dp = [[float('inf')] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    dp[r][c] = 0
        
        for r in range(rows):
            for c in range(cols):
                if dp[r][c] != float('inf'):
                    continue
                if r > 0:
                    dp[r][c] = min(dp[r][c], dp[r-1][c] + 1)
                if c > 0:
                    dp[r][c] = min(dp[r][c], dp[r][c-1] + 1)
        
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r < rows-1:
                    dp[r][c] = min(dp[r][c], dp[r+1][c] + 1)
                if c < cols-1:
                    dp[r][c] = min(dp[r][c], dp[r][c+1] + 1)
        
        return dp

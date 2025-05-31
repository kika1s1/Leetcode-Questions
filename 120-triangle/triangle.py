class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        R = len(triangle)
        dp = triangle[-1]
        for r in range(R - 2, -1, -1):
            for c in range(len(triangle[r])):
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
        
        return dp[0]
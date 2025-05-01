class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[1 for i in range(n)]  for i in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        



        # return dfs(0, 0)
        print(dp)
        return dp[m-1][n-1]
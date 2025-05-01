class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if  i >= j:
                return 0
            res = float("inf")
            for k in range(i, j):
                cost = k + max(dp(i, k - 1), dp(k + 1, j))
                res = min(res, cost)
            memo[(i, j)] = res
            return memo[(i,j)]
        return dp(1, n)

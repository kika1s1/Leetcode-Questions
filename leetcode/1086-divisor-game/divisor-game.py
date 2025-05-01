class Solution:
    def divisorGame(self, n: int) -> bool:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return False
            for i in range(1 , n // 2 + 1):
                if n % i == 0:
                    if not dfs(n-i):
                        memo[n] = True
                        return True
            memo[n] = False
            return False

        return dfs(n)
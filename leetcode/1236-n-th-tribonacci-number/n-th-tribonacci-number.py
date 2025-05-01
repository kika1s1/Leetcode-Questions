class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def trib(n):
            if n  == 0:
                return 0
            if n == 1 or n== 2:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = trib(n-1) + trib(n-2) + trib(n-3)
            return memo[n]
        return trib(n) 
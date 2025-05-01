class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(num):
            if num in memo:
                return memo[num]
            if num == 1:
                return 1
            res = 0
            for i in range(1 , num):
                res = max(res , i * (num - i) , i * dfs(num-i))
            memo[num] = res
            return res
        return dfs(n)

                                                                
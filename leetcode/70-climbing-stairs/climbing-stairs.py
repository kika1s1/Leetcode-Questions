class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ways(current, memo, target):
            if current in memo:
                return memo[current]
            if current == target:
                return 1
            if current > target:
                return 0
            one_step = ways(current+1, memo, target)
            two_step = ways(current+2, memo, target)
            memo[current] = one_step + two_step
            return one_step + two_step
        return ways(0, memo, n)
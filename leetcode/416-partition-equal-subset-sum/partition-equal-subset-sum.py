class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        memo = {}

        def dfs(index, current_sum):
            if current_sum == target:
                return True
            if current_sum > target or index == len(nums):
                return False
            key = (index, current_sum)
            if key in memo:
                return memo[key]
            memo[key] = dfs(index + 1, current_sum + nums[index]) or dfs(index + 1, current_sum)
            return memo[key]

        return dfs(0, 0)

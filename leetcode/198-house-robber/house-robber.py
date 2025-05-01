class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def house_rob(index, nums):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            rob = nums[index] + house_rob(index +2, nums)            
            not_rob = house_rob(index +1, nums)            
            memo[index] = max(rob, not_rob)
            return memo[index]
        return house_rob(0, nums)
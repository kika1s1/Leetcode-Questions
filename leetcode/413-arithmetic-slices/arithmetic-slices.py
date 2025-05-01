class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        memo = [0] * len(nums)
        res = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                memo[i] = memo[i-1] + 1
                res+= memo[i]
        
        return res
            


        
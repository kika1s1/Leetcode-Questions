class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 0
        nums.sort()
        target = nums[0]
        
        for x in nums:
            if x > target:
                target = x + 1
            else:
                result += target - x
                target += 1
        return result
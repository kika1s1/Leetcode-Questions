class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sub_sum = nums[0]
        maxim = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                sub_sum +=nums[i]
            else:
                sub_sum = nums[i]
            maxim = max(maxim, sub_sum)
        return maxim
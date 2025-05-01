class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxim = 0
        for i in range(len(nums)-1):
            maxim = max(maxim, nums[i+1]-nums[i])
        return maxim

        
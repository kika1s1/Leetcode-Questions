class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        monoc_index = []
        for index in range(len(nums)):
            if not monoc_index or nums[monoc_index[-1]] > nums[index]:
                monoc_index.append(index)
        maxim = 0
        for j in range(len(nums)-1, -1, -1):
            while monoc_index and nums[monoc_index[-1]] <= nums[j]:
                maxim = max(maxim, j-monoc_index[-1] )
                monoc_index.pop()
        return maxim
            
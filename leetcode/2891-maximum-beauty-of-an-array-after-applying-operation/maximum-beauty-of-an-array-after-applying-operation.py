class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = 0
        maxim = 1
        for i in range(len(nums)):
            while nums[s] + k < nums[i] - k:  
                s += 1
            maxim = max(maxim, i - s + 1)
        return maxim

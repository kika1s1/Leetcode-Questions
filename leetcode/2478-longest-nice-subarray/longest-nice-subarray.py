class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        prev = l = 0
        for r in range(len(nums)):
            while (prev & (prev+nums[r])) != prev:
                prev -= nums[l]
                l += 1
            prev += nums[r]
            if r - l + 1 > res:
                res = r - l + 1
        return res
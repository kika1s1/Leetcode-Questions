class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc = dec = maxim = 1

        for pos in range(len(nums) - 1):
            if nums[pos + 1] > nums[pos]:
                inc += 1
                dec = 1  
            elif nums[pos + 1] < nums[pos]:
                dec += 1
                inc = 1 
            else:
                inc = dec = 1
            maxim = max(maxim, inc, dec)

        return maxim
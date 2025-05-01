class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero, ans, start = 0, 0, 0
        for i in range(len(nums)):
            zero += nums[i] == 0
            while zero > 1:
                zero -=nums[start] == 0
                start +=1
            ans = max(ans, i -start)
        return ans

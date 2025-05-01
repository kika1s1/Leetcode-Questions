# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:

    def rob(self, nums: List[int]) -> int:
        
        
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if i-1 > 0:
                ans[i] = nums[i] + max(ans[:i-1])
            else:
                ans[i] = nums[i]
        
        return max(ans)
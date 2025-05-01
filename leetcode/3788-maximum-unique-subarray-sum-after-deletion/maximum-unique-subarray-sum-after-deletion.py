class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num > 0:
                ans +=num
        return max(nums) if ans ==0 else ans
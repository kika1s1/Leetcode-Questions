class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = float("-inf")
        summ = 0
        for num in nums:
            summ = max(num, summ + num)
            maxim = max(maxim, summ)
        return maxim
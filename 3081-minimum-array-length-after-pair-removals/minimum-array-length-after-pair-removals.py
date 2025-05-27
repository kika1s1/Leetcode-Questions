class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums[n // 2]
        cnt = bisect_right(nums, i) - bisect_left(nums, i)
        return max(n % 2, 2 * cnt - n)
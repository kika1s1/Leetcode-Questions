class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest_nums = heapq.nlargest(k, nums)
        return (largest_nums[k-1])
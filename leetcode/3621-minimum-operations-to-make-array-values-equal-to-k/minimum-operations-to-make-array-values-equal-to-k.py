class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums  = set(nums)
        minim = min(nums)
        if minim < k:
            return -1
        elif k in nums:
            return len(nums) -1
        else:
            return len(nums)
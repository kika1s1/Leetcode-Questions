class Solution:
    def countElements(self, nums: List[int]) -> int:
        k=len(nums) - nums.count(min(nums)) - nums.count(max(nums))
        if k<0:
            return 0
        return k
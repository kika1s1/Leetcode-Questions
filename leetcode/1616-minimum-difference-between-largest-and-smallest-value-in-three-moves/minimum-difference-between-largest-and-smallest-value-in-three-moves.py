class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums=sorted(nums)
        print(nums)
        if len(nums)<=4:
            return 0
        res= 1e30
        for i in range(4):
            res= min(res, nums[len(nums)-i-1]- nums[3-i])
        return res
            
            
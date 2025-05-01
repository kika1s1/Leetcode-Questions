class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        minim = float("inf")
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] >= nums[l]:
                minim = min(minim,  nums[l])
                l = mid + 1
            else:
                r = mid
        return minim 
        
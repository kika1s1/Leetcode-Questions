class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, 1
        minim = float("inf")
        while r < len(nums):
            if nums[r]-nums[l] < minim:
                minim = nums[r]-nums[l]
            l +=1
            r +=1
        return minim

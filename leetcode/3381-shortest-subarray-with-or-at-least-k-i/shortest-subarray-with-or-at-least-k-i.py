class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        first = nums[0]
        for i in range(1, len(nums)):
            first |=nums[i]
        minim = float("inf")
        if first < k:
            return -1
        def findOr(nums):
            checker = nums[0]
            for i in range(1, len(nums)):
                checker |=nums[i]
            return checker
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                sub = nums[i:j]
                l = len(sub)
                if findOr(sub) >=k:
                    minim = min(minim, l) 
            
        return minim

        
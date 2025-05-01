class Solution:
    def canSortArray(self, nums):
        bits = bin(nums[0]).count("1")
        max_seg = nums[0]
        min_seg = nums[0]
        max_prev = float("-inf")
        
        for i in range(1, len(nums)):
            if bin(nums[i]).count("1") == bits:
                max_seg = max(max_seg, nums[i])
                min_seg = min(min_seg, nums[i])
            else: 
                if min_seg < max_prev:
                    return False
                max_prev = max_seg
                max_seg = nums[i]
                min_seg = nums[i]
                bits = bin(nums[i]).count("1")
                
        if min_seg < max_prev:
            return False
        return True
    
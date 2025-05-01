class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = 0
        dec = 0
        l, r = 0, 1
        while r < len(nums):
            if nums[l] < nums[r]:
                inc +=1
            elif nums[l] > nums[r]:
                dec +=1
            l +=1
            r +=1
        if dec == 0:
            return True
        if inc == 0:
            return True
        return False

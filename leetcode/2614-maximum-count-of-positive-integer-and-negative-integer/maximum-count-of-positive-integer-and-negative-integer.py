class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = -1
        pos = -1
        l, r = 0, len(nums)-1
        # last negative
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < 0:
                neg = mid
                l = mid+1
            else:
                r = mid-1
        # last positive
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > 0:
                pos = mid
                r = mid-1
            else:
                l = mid+1
        if neg == -1 and pos == -1:
            return 0
        elif pos == -1:
            return neg +1
        elif neg == -1:
            return len(nums)-pos
        else:
            return max(neg+1, len(nums)-pos)
            
     
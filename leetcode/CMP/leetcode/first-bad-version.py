# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high-low)//2
            if isBadVersion(mid) == False:
                low = mid + 1
            elif isBadVersion(mid):
                high = mid-1
            if mid == 0 and isBadVersion(mid) == True:
                return mid
            if mid > 0 and isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid

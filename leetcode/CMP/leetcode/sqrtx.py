class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x, 
        while l <=r:
            mid = l + (r-l)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid-1
            elif mid * mid < x:
                l = mid + 1
            if mid * mid <= x and (mid+1)**2 > x:
                return mid
        
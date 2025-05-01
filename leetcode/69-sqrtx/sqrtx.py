class Solution:
    def mySqrt(self, x: int) -> int:
        best = -1
        left, right = 0, x
        while left <= right:
            mid = (left + right)//2
            if mid**2 <= x:
                best = mid
                left = mid+1
            else:
                right  = mid - 1
        return best
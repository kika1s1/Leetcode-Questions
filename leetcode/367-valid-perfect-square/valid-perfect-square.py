class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return sqrt(num) == int(sqrt(num))
        # for i in range(num+1):
        #     if i*i == num:
        #         return True
        # return False
        # s=int(num**0.5)
        # return s*s==num
        if num < 2:
            return True
        l, r = 0, num
        while l <= r:
            mid = (l + r)//2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid-1
        return False
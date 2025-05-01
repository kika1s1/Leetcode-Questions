class Solution:
    def reverse(self, x: int) -> int:
        # if x >= (2**31) - 1  or x <= (-2**31)-1:
        #     return 0
        is_pos = 1
        if x < 0:
            is_pos = -1
        ans = 0
        x = abs(x)
        while x:
            mod  = x % 10
            ans = ans *10+mod
            x //=10
        ans =  is_pos * ans
        # return
        if ans > (2**31) - 1  or ans < (-2**31)-1:
            return 0
        return ans
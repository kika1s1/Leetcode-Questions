class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        sign = -1 if num < 0 else 1
        num = abs(num)

        while num >= 7:
            r = num % 7
            num = int(num/7)
            ans = str(r) + ans
        ans = str(num) + ans
        if sign == -1:
            return "-"+ans
        else:
            return ans


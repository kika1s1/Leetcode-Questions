import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev = 0
            tem = x
            while tem != 0:
                rev = 10*rev + tem % 10
                tem = tem // 10
            return x == rev
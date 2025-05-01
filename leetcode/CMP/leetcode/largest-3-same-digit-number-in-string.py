class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            if str(digit)*3 in num:
                return str(digit)*3
        
        return ""
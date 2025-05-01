class Solution:
    def generateTheString(self, n: int) -> str:
        ans  = ''
        if n % 2 ==0:
            return "a" * (n-1) + "b"
        return "a"*n
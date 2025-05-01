class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""
        
        while a or b:
            if res[-2:] == "aa":
                res += "b"
                b -= 1
            elif res[-2:] == "bb":
                res += "a"
                a -= 1
            elif a > b:
                res += "a"
                a -= 1
            else:
                res += "b"
                b -= 1
        
        return res
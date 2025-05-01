class Solution:
    def romanToInt(self, s: str) -> int:
        s_val = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        ans = 0
        if len(s) == 1:
            return s_val[s]
        l, r = 0, 1
        out = False
        while r < len(s):
            if s[l]+s[r] in s_val:
                ans +=s_val[s[l]+s[r]]
                l = r+1
                r +=2
                if r >=len(s) and l < len(s):
                    out = True
            else:
                ans +=s_val[s[l]]
                l +=1
                r +=1
                if r >=len(s):
                    out = True
        if out:
            ans +=s_val[s[l]]
        return ans
        
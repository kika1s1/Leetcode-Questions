class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i, j in enumerate(s):
            if j.isnumeric():
                ans += (chr(ord(s[i-1])+int(j)))

            else:
                ans += j
        return ans
                
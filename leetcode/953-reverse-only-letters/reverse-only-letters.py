class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = list(s)
        l, r = 0, len(s)-1
        while l <=r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                r -=1
                l +=1
            if not s[l].isalpha():
                l +=1
            if not s[r].isalpha():
                r -=1
        return "".join(s)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        used = False
        while l <= r:
            if s[l] == s[r]:
                l +=1
                r -=1
            elif s[l] != s[r] and not used:
                used = True
                l +=1
            else:
                break
        if l > r:
            return True
        l, r = 0, len(s)-1
        used = False
        while l <= r:
            if s[l] == s[r]:
                l +=1
                r -=1
            elif s[l] != s[r] and not used:
                used = True
                r -=1
            else:
                break
        if l > r:
            return True
        return False
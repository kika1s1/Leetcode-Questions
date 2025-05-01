class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        l, r = 0, 0
        cnt = 0
        while l < len(s) and r < len(t) and cnt < 2:
            if s[l] != t[r]:
                l +=1
                cnt +=1
            else:
                l +=1
                r +=1
        return l - cnt
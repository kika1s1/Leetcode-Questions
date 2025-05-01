class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l_t = len(t)
        l_s = len(s)
        l, r = 0,0
        cnt = 0
        while l < l_t and r < l_s:
            if t[l] == s[r]:
                cnt +=1
                l +=1
                r +=1
            else:
                r +=1
        return l_t-cnt



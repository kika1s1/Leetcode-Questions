class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        N = len(s)
        l, r  = 0, 1
        while r < N:
            if s[l] > s[r] and int(s[l])%2 == int(s[r])%2:
                s[l], s[r] = s[r], s[l]
                break
            l +=1
            r +=1
        return "".join(s)
        
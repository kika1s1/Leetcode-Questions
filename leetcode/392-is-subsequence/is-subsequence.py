class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        cnt = 0
        S = len(s)
        N = len(t)
        for i in range(N):
            l = i
            while l < N and r < S:
                if s[r] == t[l]:
                    cnt +=1
                    r +=1
                    l +=1
                else:
                    l +=1
            if cnt == S:
                return True
            cnt = 0
            r = 0
            
        return True if s == t else False


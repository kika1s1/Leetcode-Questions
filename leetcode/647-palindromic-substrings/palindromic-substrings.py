class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        N  = len(s)
        for i in range(N):
            for j in range(i+1, N+1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    cnt +=1
        return cnt
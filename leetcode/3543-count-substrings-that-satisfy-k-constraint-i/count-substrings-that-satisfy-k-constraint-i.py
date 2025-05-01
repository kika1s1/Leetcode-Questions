class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub = s[i:j]
                if sub.count("0") <=k or sub.count("1") <=k:
                    cnt +=1
        return cnt
       
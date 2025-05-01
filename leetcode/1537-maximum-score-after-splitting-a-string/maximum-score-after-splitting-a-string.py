class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        ones = s.count("1")
        ans = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                zero +=1
            else:
                ones -=1
            ans = max(ans, zero + ones)
        return ans



            

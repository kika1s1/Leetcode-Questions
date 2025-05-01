class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [["" for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
        
        lcs = dp[m][n] 
        i, j = 0, 0
        scs = ""
        
        for c in lcs:
            while i < len(str1) and str1[i] != c:
                scs += str1[i]
                i += 1
            while j < len(str2) and str2[j] != c:
                scs += str2[j]
                j += 1
            
            scs += c  
            i += 1
            j += 1
        
        scs += str1[i:] + str2[j:]
        
        return scs

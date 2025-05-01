# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [{} for i in range(len(t) + 1)]
        for i in range(len(t) - 1, -1, -1):
            dp[i] = dp[i + 1].copy()
            dp[i][t[i]] = i + 1
        print(dp)
        i = 0
        for c in s:
            if c in dp[i]:
                i = dp[i][c]
            else:
                return False
        return True
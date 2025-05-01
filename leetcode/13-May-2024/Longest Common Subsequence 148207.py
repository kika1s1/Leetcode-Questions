# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l_1 = len(text1)
        l_2 = len(text2)
        memo = {}
        def LCS(text1, text2, i, j):
            if i == 0 or j == 0:
                return 0
            if (i,j) in memo:
                return memo[(i, j)]
            if text1[i-1] == text2[j-1]:
                result = 1 + LCS(text1, text2, i-1, j-1)
            else:
                result = max(LCS(text1, text2, i, j-1), LCS(text1, text2, i-1, j))
            memo[(i, j)] = result
            return result
        return LCS(text1, text2, l_1, l_2)
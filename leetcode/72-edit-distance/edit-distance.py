class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def backtrack(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if word1[i] == word2[j]:
                memo[(i, j)] = backtrack(i + 1, j + 1)
            else:
                insert = 1 + backtrack(i, j+1)
                delete = 1 + backtrack(i+1, j)
                replace = 1 + backtrack(i+1, j+1)
                memo[(i,j)] = min(insert, replace, delete)
            return memo[(i, j)]
        return backtrack(0, 0)
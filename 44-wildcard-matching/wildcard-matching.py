class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(index1, index2):
            if (index1, index2) in memo:
                return memo[(index1, index2)]
            if index1 == len(s) and index2 == len(p):
                return True
            if index1 > len(s) or index2 >= len(p):
                return False
            if p[index2] == "*":
                memo[(index1, index2)] =  dfs(index1+1, index2) or dfs(index1+1, index2+1) or dfs(index1, index2+1)
                return memo[(index1, index2)]
            elif p[index2] == "?":
                memo[(index1, index2)] = dfs(index1+1, index2+1)
                return memo[(index1, index2)]
            elif index1 < len(s) and p[index2] !=s[index1]:
                return False
            else:
                memo[(index1, index2)] = dfs(index1+1, index2+1)
                return memo[(index1, index2)]
        return dfs(0, 0)

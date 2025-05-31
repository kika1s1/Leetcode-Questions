class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) !=len(s3):
            return False
        @cache
        def dp(i, j, index):
            if len(s1) == i:
                return s3.endswith(s2[j:])
            if len(s2) == j:
                return s3.endswith(s1[i:])
            if index >= len(s3):
                return False
            if s1[i] == s2[j]== s3[index]:
                return dp(i+1, j, index+1) or dp(i, j+1, index+1)
            elif  s1[i]== s3[index]:
                return dp(i+1, j, index+1)
            elif s2[j] == s3[index]:
                return dp(i, j+1, index+1)
            else:
                return False
        return dp(0, 0, 0)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            exist = True
            for j in range(len(needle)):
                if haystack[i+j] !=needle[j]:
                    exist = False
                    break
            else:
                return i
        return -1
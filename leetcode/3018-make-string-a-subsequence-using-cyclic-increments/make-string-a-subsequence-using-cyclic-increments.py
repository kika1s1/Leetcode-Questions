class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l, r = 0, 0
        while l < len(str1) and r < len(str2):
            if str1[l] == "z" and str2[r] =="a" or (ord(str2[r]) - ord(str1[l]) == 1) or str1[l] == str2[r]:
                l +=1
                r +=1
            else:
                l +=1
        return r == len(str2)
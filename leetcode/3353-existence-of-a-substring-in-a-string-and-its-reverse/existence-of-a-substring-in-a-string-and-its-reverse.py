class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                sub = s[j:2+j]
                print(sub)
                if sub[::-1] in s and len(sub) == 2:
                    return True
        return False
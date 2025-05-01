class Solution:
    def minLength(self, s: str) -> int:
        while ("AB" in s or "CD" in s):
            s = s.replace("AB", "", 1)
            s = s.replace("CD", "", 1)
        return len(s)
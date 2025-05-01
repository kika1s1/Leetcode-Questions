class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        char = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in char:
                return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key = len)
        return s
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        chars = set(s)
        for i, char in enumerate(s):
            if char.swapcase() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
            
                if len(left) >= len(right):
                    return left
                
                else:
                    return right
        
        return s
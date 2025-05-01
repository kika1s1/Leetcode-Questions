from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        count_t = Counter(t)
        count_s = Counter()
        left = 0
        best = float("inf")
        start = -1
        required = len(count_t)  
        formed = 0
        for right in range(len(s)):
            count_s[s[right]] += 1
            
            if count_s[s[right]] == count_t[s[right]]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < best:
                    best = right - left + 1
                    start = left
                
                count_s[s[left]] -= 1
                if count_s[s[left]] < count_t[s[left]]:
                    formed -= 1
                left += 1
        
        return "" if start == -1 else s[start:start + best]

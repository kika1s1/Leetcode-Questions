class Solution:
    def balancedString(self, s: str) -> int:
        counter = collections.Counter(s)
        n = len(s) // 4
        extras = {}
        for key in counter:
            if counter[key] > n:
                extras[key] = counter[key] - n
        
        if not extras: return 0
        i = 0
        res = len(s)
        for j in range(len(s)):
            if s[j] in extras:
                extras[s[j]] -= 1
            
            while max(extras.values()) <= 0:
                res = min(res, j-i+1)
                if s[i] in extras:
                    extras[s[i]] += 1
                i += 1
                
                
        return res
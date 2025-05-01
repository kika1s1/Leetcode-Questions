class Solution:
    def findValidPair(self, s: str) -> str:
        rep = Counter(s)
        for i in range(1, len(s)):
            if s[i] !=s[i-1] and int(s[i]) == rep[s[i]] and int(s[i-1]) == rep[s[i-1]]:
                return s[i-1]+s[i]
        return ""
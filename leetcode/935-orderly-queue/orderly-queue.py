class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1: 
            return ''.join(sorted(s))
        m = s
        for i in range(1, len(s)):
            m = min(m, s[i: ]+s[: i])
        return m
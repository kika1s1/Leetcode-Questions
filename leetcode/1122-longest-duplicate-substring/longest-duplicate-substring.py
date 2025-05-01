import random
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        mod = 2**63 - 1
        base = random.randint(26, 100)
        def search(length):
            h = 0
            for i in range(length):
                h = (h * base + ord(s[i])) % mod
            seen = {h}
            power = pow(base, length, mod)
            for i in range(1, n - length + 1):
                h = (h * base - ord(s[i - 1]) * power + ord(s[i + length - 1])) % mod
                if h in seen:
                    return i
                seen.add(h)
            return -1
        
        left, right = 1, n
        start = -1
        max_len = 0

        while left < right:
            mid = (left + right) // 2
            idx = search(mid)
            if idx != -1:
                left = mid + 1
                start = idx
                max_len = mid
            else:
                right = mid
        return s[start:start + max_len] if start != -1 else ""

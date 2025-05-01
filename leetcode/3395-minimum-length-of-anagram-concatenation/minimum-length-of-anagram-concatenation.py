class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for i in range(1, n):
            if n % i == 0:
                substr = sorted(s[:i])
                if all(sorted(s[j:j+i]) == substr for j in range(i, n, i)):
                    return i
        return n
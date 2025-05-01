class Solution:
    def numSquares(self, n: int) -> int:
        
        cache = [n] * (n + 1)
        cache[0] = 0
        
        for i in range(1, n + 1):
            for s in range(1, i + 1):
                square = s * s
                if i - square < 0:
                    break
                if 1 + cache[i - square] < cache[i]:
                    cache[i] = 1 + cache[i - square]

        return cache[n]
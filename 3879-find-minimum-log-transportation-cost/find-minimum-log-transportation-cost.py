class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n > k:
            return k*(n-k)
        elif m > k:
            return k * (m-k)
        return 0
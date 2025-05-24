class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high -low+1)//2) + (1 if low % 2 == high%2== 1 else 0) 
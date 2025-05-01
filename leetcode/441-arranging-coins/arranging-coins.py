class Solution:
    def arrangeCoins(self, n: int) -> int:
        # x**2 + x = 2*n
        b = 2*n
        # r1 = (-1 - (sqrt(1+(4*b) )))//2
        r2 = (-1 + (sqrt(1+(4*b ))))//2
        
        return int(r2)
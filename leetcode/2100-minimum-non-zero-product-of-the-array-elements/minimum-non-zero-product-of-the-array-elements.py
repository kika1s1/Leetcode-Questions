
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7
        end = 2**p -1
        return ((pow(end-1, end//2, mod)) * end)  % mod
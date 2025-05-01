# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int, mask = 4294967295, 4294967295
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        return a if a <= max_int else ~(a ^ mask)
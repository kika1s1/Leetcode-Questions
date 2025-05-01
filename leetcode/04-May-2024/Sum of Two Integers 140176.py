# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mod = 2047
        while b:
            a = a & mod
            b = b & mod
            Xor = (a^b)
            And = a&b
            a = Xor
            b= (And<<1)

        return a if a<1024 else a|~mod
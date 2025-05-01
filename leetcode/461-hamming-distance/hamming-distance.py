class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        return diff.bit_count()
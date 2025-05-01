class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = start ^ goal
        return num.bit_count()
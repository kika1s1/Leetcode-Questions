# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        num_bits = num.bit_length()
        bitmask = (1 << num_bits) - 1
        return num ^ bitmask
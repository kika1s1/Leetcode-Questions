class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        num_bits = n.bit_length() if n != 0 else 1
        bitmask = (1 << num_bits) - 1
        return n ^ bitmask
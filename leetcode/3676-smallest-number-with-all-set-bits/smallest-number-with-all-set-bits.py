class Solution:
    def smallestNumber(self, n: int) -> int:
        bits = []
        n = bin(n)[2:]
        for i in n:
            bits.append("1")
        bits = "".join(bits)
        return int(bits, 2)
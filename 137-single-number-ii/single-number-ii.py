class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_count = [0] * 32  
        for num in nums:
            for i in range(32):
                if num >> i & 1:
                    bit_count[i] += 1

        ans = 0
        for i in range(32):
            if bit_count[i] % 3 != 0:
                ans |= (1 << i)
        if ans >= 2**31:
            ans -= 2**32
        return ans
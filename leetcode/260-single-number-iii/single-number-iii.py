class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        set_bit = xor_all & -xor_all
        unique1 = 0
        unique2 = 0
        for num in nums:
            if num & set_bit:
                unique1 ^= num
            else:
                unique2 ^= num
        
        return [unique1, unique2]
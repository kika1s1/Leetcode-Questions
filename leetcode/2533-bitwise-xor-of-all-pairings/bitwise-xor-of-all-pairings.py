from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0

        for num in nums1:
            xor1 ^= num

        for num in nums2:
            xor2 ^= num

        if len(nums2) % 2 == 0 and len(nums1) % 2 == 0:
            return 0 
        elif len(nums2) % 2 == 0:
            return xor2  
        elif len(nums1) % 2 == 0:
            return xor1  
        else:
            return xor1 ^ xor2 

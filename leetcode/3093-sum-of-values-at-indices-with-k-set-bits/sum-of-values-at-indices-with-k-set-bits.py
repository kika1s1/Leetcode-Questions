# class Solution:
#     def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
#         sumElement = 0
#         for i, num in enumerate(nums):
#             if bin(i)[2:].count("1") == k:
#                 sumElement += num
#         return sumElement
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0
        for i, n in enumerate(nums):
            if i.bit_count() == k:
                result += n
        return result
    
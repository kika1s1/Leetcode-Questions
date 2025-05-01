class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table  = {}
        for i, num in enumerate(nums):
            left = target - num
            if num in table:
                return [table[num], i]
            else:
                table[left] = i
            

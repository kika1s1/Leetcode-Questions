class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_element = min(nums)
        
        return sum(nums) - len(nums) * min_element
        
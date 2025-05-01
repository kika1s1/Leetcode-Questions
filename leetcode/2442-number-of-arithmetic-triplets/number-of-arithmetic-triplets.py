class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        return sum([1 for i in nums if i-diff in nums and i+diff in nums])
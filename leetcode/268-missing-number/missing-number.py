class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        upto = (N*(N+1))//2
        tot = sum(nums)
        return upto - tot
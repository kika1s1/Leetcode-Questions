class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for num in nums:
            mul *= num
        return mul // abs(mul) if mul != 0 else 0
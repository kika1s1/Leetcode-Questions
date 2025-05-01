class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        for num in nums:
            if num < 10:
                single_sum +=num
        left = sum(nums) - single_sum
        return True if left !=single_sum else False
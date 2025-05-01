class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum  = []
        for num in nums:
            if not prefix_sum:
                prefix_sum.append(num)
            else:
                prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
        
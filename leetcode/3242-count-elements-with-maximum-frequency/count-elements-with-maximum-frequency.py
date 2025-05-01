class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        rep = list(Counter(nums).values())
        maxim = max(rep)
        return maxim * rep.count(maxim)
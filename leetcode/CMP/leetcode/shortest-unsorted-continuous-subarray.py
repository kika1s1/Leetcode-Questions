class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        nums_copy = sorted(nums)
        diff = []
        for i in range(len(nums)):
            diff.append(abs(nums[i]-nums_copy[i]))
        prev = 0
        end = 0
        for i, j in enumerate(diff):
            if j > 0:
                prev = i
                break
        for i, j in enumerate(diff):
            if j > 0:
                end = i
        return 0 if end-prev == 0 else (end-prev) + 1
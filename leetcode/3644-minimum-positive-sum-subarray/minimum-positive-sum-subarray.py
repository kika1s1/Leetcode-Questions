class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minim  = float("inf")
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                diff = abs(i-j)
                sub  = nums[i:j]
                if l <=diff <=r:
                    if sum(sub) > 0:
                        minim = min(minim, sum(sub))
        if minim == float("inf"):
            return -1
        return minim
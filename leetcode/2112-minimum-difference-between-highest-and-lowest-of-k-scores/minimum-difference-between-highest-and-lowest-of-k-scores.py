class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minim = max(nums)
        for i in range(len(nums)-k+1):
            diff = abs(nums[i]-nums[i+k-1])
            minim = min(minim, diff)
        return minim
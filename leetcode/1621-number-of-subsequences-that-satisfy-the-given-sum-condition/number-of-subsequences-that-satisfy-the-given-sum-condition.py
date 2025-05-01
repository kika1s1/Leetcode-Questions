class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 +7
        result = 0
        nums.sort()
        left,right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result+ pow(2, right-left,mod))% mod
                left += 1
            else:
                right -= 1
        return result
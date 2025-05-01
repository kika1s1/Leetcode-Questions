class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                subarray = nums[:i] + nums[j:]
                if subarray == sorted(subarray) and len(subarray) == len(set(subarray)):
                    count += 1
        return count
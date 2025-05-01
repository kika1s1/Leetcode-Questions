class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = len(nums)-1
        for i in range(start, -1, -1):
            if nums[i] + i >=start:
                start = i
        return start == 0
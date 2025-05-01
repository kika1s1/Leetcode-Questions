class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] +=nums[i-1]
        cnt  = 0
        for i in nums:
            if i == 0:
                cnt +=1
        return cnt

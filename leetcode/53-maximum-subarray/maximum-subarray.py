class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = float("-inf")
        cnt = 0
        for index in range(len(nums)):
            cnt +=nums[index]
            if cnt < 0:
                maxim = max(maxim, cnt)
                cnt = 0
            else:
                maxim = max(maxim, cnt)
        return maxim
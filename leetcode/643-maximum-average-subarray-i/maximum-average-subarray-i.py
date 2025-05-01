class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cnt = 0
        maxim = float("-inf")
        average = float("-inf")
        for i in range(len(nums)):
            cnt += nums[i]
            if i >= k:
                cnt -=nums[i-k]
                maxim = max(maxim, cnt)
                average = max(average, maxim/k)
            if i ==k-1:
                maxim = max(maxim, cnt)
                average = max(average, maxim/k)
        return average
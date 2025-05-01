class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        loop = (len(nums) - k)+1
        if k == 1:
            return float(max(nums))
        windowSize = k
        s = sum(nums[0:windowSize])
        maxAv = s/k
        for i in range(k, len(nums)):

            s += nums[i]-nums[i-k]
            if s/k > maxAv:
                maxAv = s/k
        return maxAv

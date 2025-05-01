class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        diff = []
        maxim = 0
        for i in range(len(nums)):
            if i == 0:
                maxim = nums[i]
            else:
                maxim = max(maxim, nums[i])
            diff.append(maxim - nums[i])
        maxim = nums[-1]
        ans = 0
        for i in range(len(nums)-1, 0, -1):
            maxim = max(maxim, nums[i])
            ans = max(ans, diff[i-1] * maxim)
        return ans


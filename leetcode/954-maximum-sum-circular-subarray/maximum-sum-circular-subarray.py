class Solution:
    def maxSubarraySumCircular(self, nums):
        n = len(nums)
        rightMax = [0] * n
        rightMax[n - 1] = nums[n - 1]
        suffixSum = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffixSum += nums[i]
            rightMax[i] = max(rightMax[i + 1], suffixSum)

        maxSum = nums[0]
        specialSum = nums[0]
        curMax = 0
        prefixSum = 0

        for i in range(n):
            curMax = max(curMax, 0) + nums[i]
            maxSum = max(maxSum, curMax)

            prefixSum += nums[i]
            if i + 1 < n:
                specialSum = max(specialSum, prefixSum + rightMax[i + 1])

        return max(maxSum, specialSum)

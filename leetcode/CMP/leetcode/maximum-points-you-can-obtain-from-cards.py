class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        totalSum = 0
        minSubarray = 0

        for i in range(n):
            totalSum += cardPoints[i]
            minSubarray += cardPoints[i] if i < n - k else 0

        currSum = minSubarray
        for i in range(n - k, n):
            currSum = currSum - cardPoints[i - (n - k)] + cardPoints[i]
            minSubarray = min(minSubarray, currSum)

        return totalSum - minSubarray

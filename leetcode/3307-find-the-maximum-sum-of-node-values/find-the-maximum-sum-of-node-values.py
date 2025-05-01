class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        totalSum = 0
        count = 0
        positiveMin = float("inf")
        negativeMax = float("-inf")

        for nodeValue in nums:
            nodeValAfterOperation = nodeValue ^ k

            totalSum += nodeValue
            netChange = nodeValAfterOperation - nodeValue

            if netChange > 0:
                positiveMin = min(positiveMin, netChange)
                totalSum += netChange
                count += 1
            else:
                negativeMax = max(negativeMax, netChange)

        if count % 2 == 0:
            return totalSum
        return max(totalSum - positiveMin, totalSum + negativeMax)
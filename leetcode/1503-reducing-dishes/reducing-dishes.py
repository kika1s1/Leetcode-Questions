class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        maxim = 0
        satisfaction.sort()
        for i in range(len(satisfaction)):
            total = 0
            for j in range(i, len(satisfaction)):
                total +=satisfaction[j] * ((j-i)+1)
            maxim = max(maxim, total)
        return maxim
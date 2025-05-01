class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        (memo := [i[0] for i in points]).sort(reverse= True)

        return max(memo[i-1] - memo[i]for i in range(1, len(memo)))
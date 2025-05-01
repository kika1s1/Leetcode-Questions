class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        corrected = sorted(heights)
        cnt = 0
        for i, j in zip(corrected, heights):
            if i !=j:
                cnt +=1
        return cnt
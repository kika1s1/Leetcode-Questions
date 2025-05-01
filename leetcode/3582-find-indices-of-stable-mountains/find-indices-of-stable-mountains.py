class Solution:
    def stableMountains(self, height, threshold):
        ans = []
        N = len(height)
        for i in range(N):
            if height[i] > threshold and i +1 < N:
                ans.append(i+1)
        return ans
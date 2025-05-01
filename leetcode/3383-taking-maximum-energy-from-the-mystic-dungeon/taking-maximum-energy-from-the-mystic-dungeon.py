class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [float("-inf")] * len(energy)
        for i in range(len(energy)):
            if i -k >=0:
                dp[i] = max(dp[i-k] + energy[i], energy[i])
            else:
                dp[i] = energy[i]
        return max(dp[len(energy)-k:])
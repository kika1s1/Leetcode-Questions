class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        dp = [[inf] * (1 << n) for _ in range(n + 1)]
        dp[0][0] = 0
        for i, x in enumerate(nums1, 1):
            for j in range(1 << n):
                for k in range(n):
                    if j >> k & 1:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j ^ (1 << k)] + (x ^ nums2[k]))
        return dp[-1][-1]
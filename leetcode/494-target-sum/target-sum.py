class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = defaultdict(int)
        d[0] = 1

        for num in nums:
            dp = defaultdict(int)
            for k, v in d.items():
                dp[k + num] += v
                dp[k - num] += v
            d = dp

        return d[target]
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        ans = 0
        for i in range(1, n - 1):
            left = prefix[i]
            low = bisect.bisect_left(prefix, 2 * left, i + 1, n)
            high = bisect.bisect_right(prefix, (prefix[-1] + left) // 2, low, n)
            ans += max(0, high - low)
            ans %= MOD
        return ans

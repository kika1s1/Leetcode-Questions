class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d_sum = defaultdict(int)
        d_sum[0] = 1
        res = prefix = 0
        for num in nums:
            prefix += num
            res += d_sum[prefix - goal]
            d_sum[prefix] += 1
        return res
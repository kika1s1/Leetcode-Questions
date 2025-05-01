class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = 0
        for num in nums:
            total_sum = (total_sum + num) % p
        target = total_sum % p
        if target == 0:
            return 0
        mod_map = {0: -1}
        current_sum = 0
        min_len = n

        for i in range(n):
            current_sum = (current_sum + nums[i]) % p
            needed = (current_sum - target + p) % p
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])
            mod_map[current_sum] = i

        return -1 if min_len == n else min_len

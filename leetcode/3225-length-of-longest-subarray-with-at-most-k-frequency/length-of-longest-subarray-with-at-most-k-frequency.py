class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        repeated = {}
        cnt = 0
        prev = 0
        maxim = 0
        for i in range(len(nums)):
            char = nums[i]
            if char in repeated:
                repeated[char] += 1
            else:
                repeated[char] = 1
            cnt += 1
            while repeated[char] > k:
                repeated[nums[prev]] -= 1
                cnt -= 1
                prev += 1
            maxim = max(maxim, cnt)
        return maxim

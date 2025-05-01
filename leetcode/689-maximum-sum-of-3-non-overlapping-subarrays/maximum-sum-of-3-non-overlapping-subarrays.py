class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        window_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sum[0] = current_sum
        
        for i in range(1, len(window_sum)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = current_sum
        
        left = [0] * len(window_sum)
        max_idx = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[max_idx]:
                max_idx = i
            left[i] = max_idx
        
        right = [0] * len(window_sum)
        max_idx = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[max_idx]:
                max_idx = i
            right[i] = max_idx
        
        max_sum = 0
        result = [-1, -1, -1]
        for middle in range(k, len(window_sum) - k):
            l, r = left[middle - k], right[middle + k]
            total = window_sum[l] + window_sum[middle] + window_sum[r]
            if total > max_sum:
                max_sum = total
                result = [l, middle, r]
            elif total == max_sum:
                result = min(result, [l, middle, r]) 
        return result
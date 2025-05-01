class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0
        begin = 0
        end = 0
        num_to_index = {}
        while end < len(nums):
            curr_num = nums[end]
            last_occurrence = num_to_index.get(curr_num, -1)
            while begin <= last_occurrence or end - begin + 1 > k:
                current_sum -= nums[begin]
                begin += 1
            num_to_index[curr_num] = end
            current_sum += nums[end]
            if end - begin + 1 == k:
                ans = max(ans, current_sum)
            end += 1
        return ans
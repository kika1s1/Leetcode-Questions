class Solution:
    def countCompleteSubarrays(self, nums):
        unique_count = len(set(nums))
        elem_freq = Counter()
        total_subarrays, length = 0, len(nums)
        start_index = 0
      
        for end_index, value in enumerate(nums):
            elem_freq[value] += 1
            while len(elem_freq) == unique_count:
                total_subarrays += length - end_index
                elem_freq[nums[start_index]] -= 1
                if elem_freq[nums[start_index]] == 0:
                    elem_freq.pop(nums[start_index])
                start_index += 1
      
        return total_subarrays
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums 

        length = len(nums)
        result = [-1] * (length - k + 1)
        consecutive_count = 1  
        for index in range(length - 1):
            if nums[index] + 1 == nums[index + 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1  
            if consecutive_count == k:
                result[index - k + 2] = nums[index + 1]
                consecutive_count -=1

        return result
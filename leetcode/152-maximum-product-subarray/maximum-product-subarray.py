class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = nums[0]
        min_pro = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            temp_max = max(nums[i], max_pro * nums[i], min_pro * nums[i])
            temp_min = min(nums[i], max_pro * nums[i], min_pro * nums[i])
            
            max_pro = temp_max
            min_pro = temp_min
            
            result = max(result, max_pro)
        
        return result
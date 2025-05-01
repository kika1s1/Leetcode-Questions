class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort() 
        left, right = 0, len(nums) - 1
        
        while left < right:
            total = nums[left] + nums[right]
            
            if total == 0:
                return max(nums[left], -nums[left])
            elif total < 0:
                left += 1
            else:
                right -= 1
        
        return -1

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        curr_sum = sum(nums[l:r])
        max_avg = curr_sum / k
        
        while r < len(nums):
            curr_sum += nums[r] - nums[l]
            avg = curr_sum / k
            max_avg = max(max_avg, avg)
            r += 1
            l += 1
        
        return max_avg
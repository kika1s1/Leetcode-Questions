class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        cnt = 0
        min_queue = [nums[0]] 
        max_queue = [nums[0]] 
        if len(nums) == 1:
            return 1
        
        for end in range(1, len(nums)): 
            while min_queue and   nums[end] < min_queue[-1]:
                min_queue.pop()
            min_queue.append(nums[end])
            
            while max_queue and  nums[end] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[end])
            
            while max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[start]:
                    max_queue.pop(0)
                if min_queue[0] == nums[start]:
                    min_queue.pop(0)
                start += 1
            
            cnt = max(cnt, end - start + 1)
        
        return cnt
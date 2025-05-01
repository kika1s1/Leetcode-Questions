class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        left = 0
        maxim_length = 0
        for r in range(len(nums)):
            while max_queue and max_queue[-1] < nums[r]:
                max_queue.pop()
            max_queue.append(nums[r])
            while min_queue and min_queue[-1] > nums[r]:
                min_queue.pop()
            min_queue.append(nums[r])
            while max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left +=1
            maxim_length = max(maxim_length, r-left + 1 )
        return maxim_length




class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = []
        max_n = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(h, (nums[i][0], i, 0))
            max_n = max(max_n, nums[i][0])
        
        start, end = -1, float('inf')

        while h:
            min_n, list_idx, elem_idx = heapq.heappop(h)
            
            if max_n - min_n < end - start:
                start, end = min_n, max_n
            
            if elem_idx + 1 < len(nums[list_idx]):
                next_n = nums[list_idx][elem_idx + 1]
                heapq.heappush(h, (next_n, list_idx, elem_idx + 1))
                max_n = max(max_n, next_n)
            else:
                break
        
        return [start, end]

# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap,  -i)


    
        for i in range(k-1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)
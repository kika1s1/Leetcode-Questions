class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap  = []
        for num in nums:
            heappush(heap, num)
        operations = 0
        while heap[0] < k:
            operations +=1
            f = heappop(heap)
            s = heappop(heap)
            heappush(heap, min(s, f)*2 + max(f, s))
        return operations
            
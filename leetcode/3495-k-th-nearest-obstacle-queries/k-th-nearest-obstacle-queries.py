class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []
        ans = []
        for i,j in queries:
            heapq.heappush(heap, -(abs(i) + abs(j)))
            if len(heap) > k:
                heapq.heappop(heap)
            ans.append(-heap[0] if len(heap) == k else -1)
        return ans
        
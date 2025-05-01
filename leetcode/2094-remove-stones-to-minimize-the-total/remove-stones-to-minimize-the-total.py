class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapify(heap)
        for i in range(k):
            removed = heappop(heap)
            heappush(heap, (removed + (-(removed)//2)))
        return - (sum(heap))
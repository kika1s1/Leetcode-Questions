class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        l, r = 0, len(costs) - 1
        res = 0
        pq2, pq1 = [], []

        while k:

            while len(pq1) < candidates and l <= r:
                heapq.heappush(pq1, costs[l])
                l += 1

            while len(pq2) < candidates and l <= r:
                heapq.heappush(pq2, costs[r])
                r -= 1

            if len(pq1) == 0:
                heapq.heappush(pq1, float("inf"))
            elif len(pq2) == 0:
                heapq.heappush(pq2, float("inf"))

            res += heapq.heappop(pq1) if pq1[0] <= pq2[0] else heapq.heappop(pq2)           
            k -= 1

        return res
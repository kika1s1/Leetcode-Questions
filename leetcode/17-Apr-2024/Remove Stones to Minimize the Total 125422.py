# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            max_pile = heapq.heappop(piles)
            heapq.heappush(piles, max_pile // 2)
        tot = 0
        for i in piles:
            tot += -i
        return tot
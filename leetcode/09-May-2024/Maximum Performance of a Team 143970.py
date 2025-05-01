# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for eff, spd in zip(efficiency, speed):
            eng.append([eff, spd])
        eng.sort(reverse=True)
        res, speed = 0, 0
        minHeap = []
        for eff, spd in eng:
            if len(minHeap) == k:
                speed -= heappop(minHeap)
            speed +=spd
            heappush(minHeap, spd)
            res = max(res, eff * speed)
        return res % ((10 **9) + 7)
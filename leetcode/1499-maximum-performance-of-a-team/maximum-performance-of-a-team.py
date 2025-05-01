class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = sorted([[eff, spd] for eff, spd in zip(efficiency, speed)], key=lambda x:-x[0])
        res, speed = 0, 0
        minHeap = []
        for eff, spd in eng:
            if len(minHeap) == k:
                speed -= heappop(minHeap)
            speed +=spd
            heappush(minHeap, spd)
            res = max(res, eff * speed)
        return res % ((10 **9) + 7)
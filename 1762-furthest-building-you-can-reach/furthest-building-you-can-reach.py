class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heappush(heap, -diff)
                bricks -= diff
                if bricks < 0:
                    if ladders > 0:
                        bricks += -heappop(heap)
                        ladders -= 1
                    else:
                        return i - 1
        return n - 1

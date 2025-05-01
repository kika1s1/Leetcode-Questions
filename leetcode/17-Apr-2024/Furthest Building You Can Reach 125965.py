# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heappush(heap, -diff)
                bricks -= diff
                if bricks < 0 and ladders == 0:
                    return i -1
                elif bricks < 0:
                    value = heappop(heap)
                    bricks += -value
                    ladders -= 1
        return len(heights) - 1




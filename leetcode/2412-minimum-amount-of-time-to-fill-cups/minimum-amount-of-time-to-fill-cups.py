
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = [-ele for ele in amount]
        heapify(max_heap)
        seconds = 0

        while max_heap[0] != 0 : 
            ele1 = heappop(max_heap)
            ele2 = heappop(max_heap)

            if ele1 != 0 : ele1 += 1
            if ele2 != 0 : ele2 += 1

            heappush(max_heap, ele1)
            heappush(max_heap, ele2)

            seconds += 1

        return seconds 
# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        heapq.heapify(self.minHeap)
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if len(self.minHeap) > 0 and num > -self.minHeap[0]:
            heapq.heappush(self.maxHeap, num)
            if len(self.maxHeap) > len(self.minHeap):
                item = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -item)
        else:
            heapq.heappush(self.minHeap, -num)
            if len(self.minHeap) - len(self.maxHeap) > 1:
                item = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -item)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.minHeap[0] + self.maxHeap[0]) / 2
        else:
            return -self.minHeap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
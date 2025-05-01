# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.intHeap = nums
        self.k = k
        heapq.heapify(self.intHeap)
        while len(self.intHeap) > k:
            heapq.heappop(self.intHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.intHeap, val)
        while len(self.intHeap) > self.k:
            heapq.heappop(self.intHeap)
        return self.intHeap[0]

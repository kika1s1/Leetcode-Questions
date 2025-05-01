class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [x for x in range(1, 1000+1)]

    def popSmallest(self) -> int:
        val = heappop(self.heap)
        return val
        
        

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
class MedianFinder:

    def __init__(self):
        self.items = []
        

    def addNum(self, num: int) -> None:
        self.items.append(num)

    def findMedian(self) -> float:
        self.items.sort()
        mid = len(self.items)//2
        if len(self.items) % 2 ==1:
            return self.items[mid]
        else:
            return (self.items[mid] + self.items[mid-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
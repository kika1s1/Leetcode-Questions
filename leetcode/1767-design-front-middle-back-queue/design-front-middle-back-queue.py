class FrontMiddleBackQueue:
    def __init__(self):
        self.items = []
    def pushFront(self, val: int) -> None:
        self.items.insert(0, val)
    def pushMiddle(self, val: int) -> None:
        if not self.items:
            self.items.append(val)
            return
        index = len(self.items)//2
        self.items.insert(index, val)
    def pushBack(self, val: int) -> None:
        self.items.append(val)
    def popFront(self) -> int:
        if not self.items:
            return -1
        temp =  self.items.pop(0)
        return temp
    def popMiddle(self) -> int:
        if not self.items:
            return -1
        index = len(self.items)//2
        if index != len(self.items)/2:
            temp = self.items.pop(index)
            print(temp, self.items) 
            return temp
        else:
            return self.items.pop(index-1) 
    def popBack(self) -> int:
        if self.items:
            return self.items.pop()
        return -1        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
class MinStack:

    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, val: int) -> None:
        self.items.append(val)
        self.length +=1

        

    def pop(self) -> None:
        self.items.pop()
        self.length -=1

    def top(self) -> int:
        temp = self.items[-1]
        return temp

    def getMin(self) -> int:
        return min(self.items)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
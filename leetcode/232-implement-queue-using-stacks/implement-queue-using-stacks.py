class MyQueue:

    def __init__(self):
        self.items = []
        self.length = 0
        

    def push(self, x: int) -> None:
        self.items.insert(0, x)
        self.length +=1
        

    def pop(self) -> int:    
        self.length -=1
        return self.items.pop()


    def peek(self) -> int:
        return self.items[-1]
        

    def empty(self) -> bool:

        return len(self.items) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
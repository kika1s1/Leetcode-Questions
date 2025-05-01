class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.tail = None
        self.head = None
        self.length = 0
        self.k = k
        

    def insertFront(self, value: int) -> bool:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            return True
        if self.length == self.k:
            return False
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1
            return True




    def insertLast(self, value: int) -> bool:
        new_node = Node(value)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
            self.length +=1
            return True
        if self.length == self.k:
            return False
        self.tail.next = new_node
        self.tail = new_node
        print(self.tail.val)
        self.length +=1
        return True

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        if self.head == self.tail:
            self.tail, self.head = None, None
            self.length -=1
            return True
        
        if self.head:
            self.head = self.head.next
            self.length -=1
            return True




        

    def deleteLast(self) -> bool:
        if not self.tail:  
            return False
        if self.head == self.tail:  
            self.tail, self.head = None, None
            self.length -= 1
            return True
        
        prev = None
        current = self.head
        
        while current.next:
            prev = current
            current = current.next
        
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        return True


    def getFront(self) -> int:
        if not self.head:
            return -1
        return self.head.val
        

    def getRear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.length ==0
        

    def isFull(self) -> bool:
        return self.length == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
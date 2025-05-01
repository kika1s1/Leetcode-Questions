class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        node = self.head
        for i in range(index - 1):
            node = node.next
        new_node.next = node.next
        node.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:  
            self.head = self.head.next
            if not self.head:  
                self.tail = None
        elif index == self.length - 1:  
            node = self.head
            for i in range(index - 1):
                node = node.next
            node.next = None
            self.tail = node
        else:  
            node = self.head
            for i in range(index - 1):
                node = node.next
            node.next = node.next.next
        self.length -= 1

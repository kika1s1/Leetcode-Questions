class Node:
    def __init__(self, link):
        self.link = link
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = Node(homepage)
        self.tail = self.root
        self.head = self.tail
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.tail and self.tail.prev:
                self.tail = self.tail.prev
            else:
                return self.tail.link
        return self.tail.link

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.tail and self.tail.next:
                self.tail = self.tail.next
            else:
                return self.tail.link
        return self.tail.link

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
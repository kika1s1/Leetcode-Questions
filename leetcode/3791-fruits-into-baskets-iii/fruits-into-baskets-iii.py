class SegTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [-1] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, pos: int, value: int) -> None:
        pos += self.size
        self.tree[pos] = value
        pos //= 2
        while pos:
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos //= 2

    def query(self, x: int) -> int:
        if self.tree[1] < x:
            return -1
        pos = 1
        while pos < self.size:
            if self.tree[2 * pos] >= x:
                pos = 2 * pos
            else:
                pos = 2 * pos + 1
        return pos - self.size

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        seg = SegTree(baskets)
        unplaced = 0
        
        for fruit in fruits:
            idx = seg.query(fruit)
            if idx == -1:
                unplaced += 1
            else:
                seg.update(idx, -1)
        return unplaced

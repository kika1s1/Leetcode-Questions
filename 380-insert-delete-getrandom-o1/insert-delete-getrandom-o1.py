class RandomizedSet:

    def __init__(self):
        self.items = set()
    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items.add(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        self.items.discard(val)
        return True
    def getRandom(self) -> int:
        # val = self.items.pop()
        # self.items.add(val)
        return random.choice(list(self.items))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
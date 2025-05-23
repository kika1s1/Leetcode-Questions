class RandomizedSet:

    def __init__(self):
        self.items = []
        self.pos = {}
    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.items)
        self.items.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        pos_index = self.pos[val]
        self.items[pos_index] = self.items[-1]
        self.pos[self.items[-1]] = pos_index
        del self.pos[val]
        self.items.pop()
        return True

    def getRandom(self) -> int:
        # pos = randint(0, len(self.items)-1)
        return random.choice(self.items)
        # return self.items[pos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
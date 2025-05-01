class RandomizedCollection:
    def __init__(self):
        self.numbers = []
        self.indx = defaultdict(set)
    def insert(self, val: int) -> bool:
        self.indx[val].add(len(self.numbers))
        self.numbers.append(val)
        return len(self.indx[val]) == 1


    def remove(self, val: int) -> bool:
 
        if not self.indx[val]:
            return False
        indx_remove, last = self.indx[val].pop(), self.numbers[-1]
        self.numbers[indx_remove] = last
        self.indx[last].add(indx_remove)
        self.indx[last].discard(len(self.numbers) - 1)
        self.numbers.pop()
        return True


    def getRandom(self) -> int:
        return choice(self.numbers)
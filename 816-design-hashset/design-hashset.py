class MyHashSet:

    def __init__(self):
        self.map = [-1] * (10**6 + 1)
        

    def add(self, key: int) -> None:
        self.map[key] = key
        

    def remove(self, key: int) -> None:
        self.map[key] =-1
        

    def contains(self, key: int) -> bool:
        return self.map[key] ==key


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class RandomizedSet:

    def __init__(self):
        self.dic_direct = {}
        self.dic_invert = {}
        self.num_elem = 0
        
    def insert(self, val: int) -> bool:
        if val in self.dic_invert:
            return False
        else:
            self.dic_invert[val] = self.num_elem
            self.dic_direct[self.num_elem] = val
            self.num_elem += 1
            return True
        
    def remove(self, val):
        if val not in self.dic_invert:
            return False
        else:
            ind = self.dic_invert.pop(val)
            self.dic_direct.pop(ind)
            if ind != self.num_elem - 1:
                self.dic_direct[ind] = self.dic_direct[self.num_elem - 1]
                self.dic_invert[self.dic_direct[self.num_elem - 1]] = ind
                self.dic_direct.pop(self.num_elem - 1)
            self.num_elem -= 1
            return True
        
    def getRandom(self):
        index = floor(random.random()*self.num_elem)
        return self.dic_direct[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
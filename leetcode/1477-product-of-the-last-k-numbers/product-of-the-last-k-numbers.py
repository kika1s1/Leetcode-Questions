class ProductOfNumbers:
    def __init__(self):
        self.prod = [1]
        self.size = 0

    def add(self, num: int):
        if num == 0:
            self.prod = [1]
            self.size = 0
        else:
            self.prod.append(self.prod[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return (
            self.prod[self.size] // self.prod[self.size - k]
        )
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.total = sum(w)
        for num in w:
            if not self.prefix:
                self.prefix.append(num)
            else:
                self.prefix.append(self.prefix[-1] + num)
    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)
        low, high = 0, len(self.prefix) - 1
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix[mid]:
                low = mid + 1
            else:
                high = mid
        return low





# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class RecentCounter:

    def __init__(self):
        self.items = []
        

    def ping(self, t: int) -> int:
        if not self.items:
            self.items.append(t)
            return 1
        self.items.append(t)
        down = self.items[-1] - 3000
        cnt = 0
        for num in self.items[::-1]:
            if down <= num <= self.items[-1]:
                cnt +=1
            else:
                return cnt
        return cnt
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
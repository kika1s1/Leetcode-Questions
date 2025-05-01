class Solution:

    def __init__(self, nums: List[int]):
        self.items = {}
        for i,j in enumerate(nums):
            if j not in self.items:
                self.items[j] = {i}
            else:
                self.items[j].add(i)
       


    def pick(self, target: int) -> int:
        return(random.choice(list(self.items[target])))

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
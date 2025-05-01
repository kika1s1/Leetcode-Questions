class Solution:

    def __init__(self, nums: List[int]):
        self.init = nums[:]
        self.arr = nums[:]
        
    def reset(self) -> List[int]:
        # self.arr = self.init[:]
        return self.arr

    def shuffle(self) -> List[int]:
        shuffled = self.arr[:]
        random.shuffle(shuffled)
        return shuffled

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

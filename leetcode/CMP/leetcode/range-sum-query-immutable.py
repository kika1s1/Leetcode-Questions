class NumArray:

    def __init__(self, nums):
        self.nums = nums

        for i in range(len(self.nums)):
            if i != 0:
                self.nums[i] += self.nums[i-1]
    def sumRange(self, left, right):
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left-1]
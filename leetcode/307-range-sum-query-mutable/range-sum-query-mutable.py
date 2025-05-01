class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n == 0:
            return 
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n-1)
    def build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end)//2
            left_child = node * 2 +1
            right_child = node*2 + 2
            self.build(nums, left_child, start, mid)
            self.build(nums, right_child, mid+1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    def update(self, index: int, val: int, node=0, start=0, end=None) -> None:
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = val
        else:
            mid = (start+end)//2
            left_child = 2*node +1
            right_child = 2*node +2
            if index <=mid:
                self.update(index, val, left_child, start, mid)
            else:
                self.update(index, val, right_child, mid+1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def sumRange(self, left: int, right: int, node=0, start=0, end=None) -> int:
        if end is None:
            end = self.n-1
        if left <= start and end <= right:
            return self.tree[node]

        if end < left or start > right:
            return 0
        mid = (start + end) // 2
        left_sum = self.sumRange(left, right, 2 * node + 1, start, mid)
        right_sum = self.sumRange(left, right, 2 * node + 2, mid + 1, end)

        return left_sum + right_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
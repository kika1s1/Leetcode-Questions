class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_nums = []
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N+1):
                sub = sum(nums[i:j])
                sum_nums.append(sub)
        sum_nums.sort()
        return sum(sum_nums[left-1:right]) % ((10 **9) + 7)
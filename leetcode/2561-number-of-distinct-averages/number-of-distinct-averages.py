class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        res = set()
        while(i < j):
            avg = (nums[i] + nums[j]) / 2
            res.add(avg)
            i += 1
            j -= 1
        return len(res)
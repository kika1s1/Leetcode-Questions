class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in nums:
            times = nums.count(i)
            if times > 2:
                for _ in range(times-2):
                    nums.remove(i)
        return len(nums)



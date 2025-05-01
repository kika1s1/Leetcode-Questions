class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        initial = len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                nums.insert(i, target)
                break
        if len(nums) == initial:
            nums.append(target)

        return nums.index(target)
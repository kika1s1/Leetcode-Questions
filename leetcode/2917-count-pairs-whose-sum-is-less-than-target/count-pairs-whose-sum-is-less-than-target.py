class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i]+nums[j] < target:
                    count += 1
        return count
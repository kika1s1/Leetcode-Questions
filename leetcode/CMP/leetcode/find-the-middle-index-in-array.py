class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        total_sum = sum(nums)
        
        for i,num in enumerate(nums):
            total_sum -= num
            if curr_sum == total_sum:
                return i
            curr_sum+=num

        return -1
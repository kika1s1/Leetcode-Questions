class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(nums)
        a = n[len(n)-1]-1
        b = n[len(n)-2]-1  
        return a*b
        
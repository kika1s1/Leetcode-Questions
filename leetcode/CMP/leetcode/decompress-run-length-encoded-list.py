class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        final = []
        for i in range(0, len(nums),2):
            for _ in range(nums[i]):
                final.append(nums[i+1])
        return final
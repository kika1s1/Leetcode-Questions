class Solution:

    def findMaxLength(self, nums: List[int]) -> int:

        hmap = {}
        hmap[0] = 0        
        excess = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                excess += 1
            else: 
                excess -= 1
            if excess in hmap:
                max_length = max(max_length, i+1 - hmap[excess])
            else:
                hmap[excess] = i + 1       
        return max_length            
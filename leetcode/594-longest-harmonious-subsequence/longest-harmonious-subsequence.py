class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) == 1:
            return 0

        nums.sort()

        highest_len = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i]-1 in s:
                l = i-(nums.index(nums[i]-1)-1)
                if l > highest_len:
                    highest_len = l
        
        return highest_len

        return 0



        
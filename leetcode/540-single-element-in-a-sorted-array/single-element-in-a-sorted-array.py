class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:                    #only unique element
            return nums[0]

        if nums[0]!=nums[1]:                #check first element
            return nums[0]

        for i in range(1,len(nums)-1):      #check elements in middle
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]

        return nums[-1]                     #only last element will be left
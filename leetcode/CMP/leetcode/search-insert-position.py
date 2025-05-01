class Solution(object):
    def searchInsert(self, nums, target):
        left,right=0,len(nums)
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return left
        
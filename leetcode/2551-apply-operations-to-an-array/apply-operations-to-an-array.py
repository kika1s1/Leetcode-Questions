class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] =2*nums[i]
                nums[i+1] = 0
        for i in range(len(nums)-1):
            l, r = i, i +1
            if nums[l] == 0:
                while r < len(nums):
                    if nums[r] != 0:
                        nums[l], nums[r] = nums[r], nums[l]
                        l = r
                        r = l + 1
                    else:
                        r +=1
        return nums
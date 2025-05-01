class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # [7,6,5,4,3,2,1]
        # [5,6,7,3,2,1]
        l, r = 0, len(nums)-1
        while l <=r:
            nums[l], nums[r] = nums[r], nums[l]
            r -=1
            l +=1
        l = (k % len(nums))
        r = len(nums)-1
        while l  <= r:
            nums[l], nums[r] = nums[r], nums[l]
            r -=1
            l +=1
        l, k = 0, (k % len(nums))-1
        while l <=k:
            nums[l], nums[k] = nums[k], nums[l]
            l +=1
            k -=1
        
        return nums
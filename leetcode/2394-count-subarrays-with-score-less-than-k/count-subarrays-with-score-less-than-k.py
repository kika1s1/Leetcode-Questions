class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        total = 0
        for r in range(len(nums)):
            total +=nums[r]
            while total *(r-l + 1) >=k:
                total -=nums[l]
                l +=1
            ans +=(r-l +1)
        return ans

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort(reverse=True)
        ans=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                ans+=i+1
        return ans         
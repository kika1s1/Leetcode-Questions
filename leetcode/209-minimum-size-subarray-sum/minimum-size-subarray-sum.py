class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l, r = 0, 0
        rsum = 0
        minlength = float('inf')

        for r in range(len(nums)):

            rsum += nums[r]

            while rsum >= target:
                minlength = min(minlength, (r-l+1))
                rsum -= nums[l]
                l += 1


        return 0 if minlength == float('inf') else minlength



        

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        ans = 0
        maxim = max(nums)
        N = len(nums)
        l = 0
        for r in range(len(nums)):
            if nums[r] == maxim:
                cnt +=1
            while cnt >=k:
                ans +=(N-r)
                cnt -= (nums[l] == maxim)
                l +=1
        return ans
            
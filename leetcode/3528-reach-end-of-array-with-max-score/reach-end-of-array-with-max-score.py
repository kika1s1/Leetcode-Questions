class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return 0
        i = 0
        ans = 0
        prev = nums[0]
        for j in range(1, N):
            if prev < nums[j]:
                ans +=((j-i)*prev)
                prev = nums[j]
                i = j
        if i !=j:
            ans +=((j-i)*prev)
        
        return ans
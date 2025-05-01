class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        maxim = nums[0]
        ans = float("-inf")
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > maxim:
                maxim = nums[i]
                cnt +=1
                ans = max(ans, cnt)
            else:
                maxim = nums[i]
                cnt = 1
        return max(ans, cnt)

            

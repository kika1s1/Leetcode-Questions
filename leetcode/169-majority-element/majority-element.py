class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if cnt == 0:
                ans = nums[i]
                cnt = 1
            elif ans == nums[i]:
                cnt +=1
            else:
                cnt -=1
        return ans
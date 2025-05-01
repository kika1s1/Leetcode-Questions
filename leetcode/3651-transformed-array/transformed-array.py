class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[(i+nums[i])%len(nums)])
        return ans
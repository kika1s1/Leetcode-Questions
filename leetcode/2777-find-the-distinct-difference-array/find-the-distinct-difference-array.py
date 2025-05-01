class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if i !=len(nums):
                pref = nums[0:i+1]
                suffix = nums[i+1:]
            else:
                pref = nums[0:i+1]
                suffix = 0
            diff = len(set(pref))-len(set(suffix))
            ans.append(diff)
        return ans
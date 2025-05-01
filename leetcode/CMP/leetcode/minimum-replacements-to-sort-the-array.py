class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        maxim = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            step_times = (nums[i] + maxim - 1) // maxim
            ans += step_times - 1
            maxim = nums[i] // step_times
        return ans
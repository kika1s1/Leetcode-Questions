class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] = nums[i]+nums[i-1]
        ans = []
        for q in queries:
            index = bisect_right(nums, q)
            ans.append(index)
        return ans

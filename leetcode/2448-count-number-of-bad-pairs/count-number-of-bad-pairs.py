class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pair_diff = defaultdict(int)
        N = len(nums)
        for index, num in enumerate(nums):
            pair_diff[num-index] +=1
        ans = 0
        for index in range(N-1, -1, -1):
            ans +=(index + 1 - pair_diff[nums[index]-index])
            pair_diff[nums[index]-index] -=1
        return ans



        
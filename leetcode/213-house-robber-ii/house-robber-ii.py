class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        def rob_house(index, nums, memo):
            if index >= len(nums): 
                return 0
            if index in memo:
                return memo[index]
            rob = nums[index] + rob_house(index + 2, nums, memo)
            not_rob = rob_house(index + 1, nums, memo)
            memo[index] = max(rob, not_rob)
            return memo[index]

        memo1 = {}
        ans1 = rob_house(1, nums, memo1)
        memo2 = {}
        ans2 = rob_house(0, nums[:-1], memo2)
        return max(ans1, ans2)

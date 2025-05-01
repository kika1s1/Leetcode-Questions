class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(left, right):
            if left == right:
                return nums[left]

            pickLeft = nums[left] - dfs(left + 1, right)
            pickRight = nums[right] - dfs(left, right - 1)

            return max(pickLeft, pickRight)
        return dfs(0, len(nums) - 1) >= 0

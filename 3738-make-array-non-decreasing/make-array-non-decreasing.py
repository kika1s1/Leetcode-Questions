class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            elif stack[-1] <= num:
                stack.append(num)
        return len(stack)
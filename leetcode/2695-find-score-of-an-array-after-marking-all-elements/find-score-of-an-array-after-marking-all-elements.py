class Solution:
    def findScore(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(nums)):
            if not stack or nums[i] < stack[-1]:
                stack.append(nums[i])
            else:
                while stack:
                    ans +=stack.pop()
                    if stack:
                        stack.pop()
        while stack:
            ans +=stack.pop()
            if stack:
                stack.pop()
        return ans




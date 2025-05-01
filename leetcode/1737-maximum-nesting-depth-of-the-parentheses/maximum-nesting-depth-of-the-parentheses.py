class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxim = 0
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                maxim = max(maxim, len(stack))
                stack.pop()
            else:
                maxim = max(maxim, len(stack))
            
        return maxim

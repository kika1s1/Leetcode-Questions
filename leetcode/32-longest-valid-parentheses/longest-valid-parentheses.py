class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxi = 0
        for i in range(0, len(s)):
            char = s[i]
            if char == "(":
                stack.append(i)
            else:
                index = stack.pop()
                if stack:
                    maxi = max(maxi, i - stack[-1])
                else:
                    stack.append(i)
        return maxi
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for symbol in s:
            if symbol == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(symbol)
        return "".join(stack)
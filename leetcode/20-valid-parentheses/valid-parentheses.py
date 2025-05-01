class Solution:
    def isValid(self, s: str) -> bool:
        op = {")":"(", "}":"{", "]":"["}
        stack = []
        for chr in s:
            if chr not in op:
                stack.append(chr)
            else:
                if stack and stack[-1] == op[chr]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
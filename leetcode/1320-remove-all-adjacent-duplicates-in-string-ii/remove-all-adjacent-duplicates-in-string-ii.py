class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        cnt = []
        for char in s:
            if not stack:
                stack.append(char)
                cnt.append(1)
            elif stack and stack[-1] == char:
                stack.append(char)
                cnt.append(cnt[-1] + 1)
            else:
                stack.append(char)
                cnt.append(1)
            if cnt and cnt[-1] == k:
                for i in range(k):
                    stack.pop()
                    cnt.pop()
        return "".join(stack)

            
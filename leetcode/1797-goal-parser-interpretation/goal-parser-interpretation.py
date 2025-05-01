class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        stack = []
        for char in command:
            if char.isalpha():
                ans.append(char)
                if stack:
                    stack.pop()
            elif char =="(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                    ans.append("o")
        return "".join(ans)
class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char == "a" and stack[-1] == "z" or char =="z" and stack[-1] == "a":
                    stack.pop()
                else:
                    if abs(ord(char)-ord(stack[-1])) == 1:
                        stack.pop()
                    else:
                        stack.append(char)
        return "".join(stack)
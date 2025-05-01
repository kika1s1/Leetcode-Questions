class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        for i in s:
            if i !="#":
                s_stack.append(i)
            elif s_stack:
                s_stack.pop()
            else:
                continue
        t_stack = []
        for j in t:
            if j !="#":
                t_stack.append(j)
            elif t_stack:
                t_stack.pop()
            else:
                continue
        print(s_stack, t_stack)
        return t_stack == s_stack
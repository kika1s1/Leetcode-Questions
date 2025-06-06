class Solution:
    def robotWithString(self, s: str) -> str:
        left = [""] * len(s)
        stack = []
        N = len(s)
        for i in range(len(s)-1, -1, -1):
            if i == N-1:
                left[i] = s[i]
            else:
                left[i] = min(left[i+1], s[i])
        ans = []
        for i in range(N):
            while stack and stack[-1] <=left[i]:
                    ans.append(stack.pop())
            stack.append(s[i])
            
        while stack:
            ans.append(stack.pop())
        return "".join(ans)
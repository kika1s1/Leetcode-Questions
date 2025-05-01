class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lookup = {}

        for i in range(len(s)):
            lookup[s[i]] = i
        
        seen = set()
        stack = []
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and stack[-1] > s[i] and lookup[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)

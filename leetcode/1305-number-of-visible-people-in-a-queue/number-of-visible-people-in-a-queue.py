class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            height = heights[i]
            visibility = 0
            while stack and height > stack[-1]:
                stack.pop()
                visibility += 1
            if(stack):
                visibility += 1
            ans[i]=visibility
            stack.append(height)
        return ans
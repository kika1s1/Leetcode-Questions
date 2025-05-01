class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """

        [2,1, 5, 6, 2, 3]
        "0 1  2  3  4  5"
        what matters here is  minimum height and width
        [2,1]
        # [2, 3, ]
        [2, 1, 5]
        2 


            """
        stack = [] 
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area

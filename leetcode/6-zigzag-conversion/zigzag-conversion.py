class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        grid = [[] for _ in range(numRows)]
        start = 0
        direction = 1  
        for a in s:
            grid[start].append(a)
            if start == 0:
                direction = 1
            elif start == numRows - 1:
                direction = -1
                
            start += direction

        return "".join("".join(row) for row in grid)

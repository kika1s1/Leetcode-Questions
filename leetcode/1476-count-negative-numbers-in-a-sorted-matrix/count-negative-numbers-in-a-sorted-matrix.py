class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            c = -1
            
            while grid[i][c] < 0:
                cnt +=1
                c -=1
                if len(grid[i]) < -1*c:
                    break
        return cnt



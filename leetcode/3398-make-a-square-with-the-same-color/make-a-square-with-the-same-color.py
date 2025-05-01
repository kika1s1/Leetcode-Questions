class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        def isPossible(grid, i, j):
            # print(i, j)
            cnt = 0
            cnt_w = 0
            if i < ROWS and j < COLS-1:

                if grid[i][j] =="B":
                    cnt +=1
                if grid[i+1][j] =="B":
                    cnt +=1
                if grid[i][j+1]=="B":
                    cnt +=1
                if grid[i+1][j+1] =="B":
                    cnt +=1
            
                if grid[i][j] =="W":
                    cnt_w +=1
                if grid[i+1][j] =="W":
                    cnt_w +=1
                if grid[i][j+1]=="W":
                    cnt_w +=1
                if grid[i+1][j+1] =="W":
                    cnt_w +=1
            
            return cnt <=1 or cnt_w <=1
        for i in range(ROWS):
            for j in range(COLS):
                if i!=ROWS-1 and j != COLS-1:
                    if isPossible(grid, i, j):
                        return True
        return False

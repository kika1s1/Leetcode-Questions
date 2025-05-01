class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        farmlands = []
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    bottom_row = i
                    right_col = j

                    while bottom_row + 1 < rows and land[bottom_row + 1][j] == 1:
                        bottom_row += 1
                    while right_col + 1 < cols and land[i][right_col + 1] == 1:
                        right_col += 1

                    farmlands.append([i, j, bottom_row, right_col])
                    
        return farmlands
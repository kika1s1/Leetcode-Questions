from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        row_count = [0] * row
        col_count = [0] * col
        
        position = [None] * (row * col + 1) 
        for i in range(row):
            for j in range(col):
                num = mat[i][j]
                position[num] = (i, j) 
        for index, num in enumerate(arr):
            x, y = position[num]
            row_count[x] += 1
            col_count[y] += 1
            if row_count[x] == col or col_count[y] == row:
                return index
        

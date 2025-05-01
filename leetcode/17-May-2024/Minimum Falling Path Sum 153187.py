# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j):
            if j < 0 or j >= COLS:
                return float('inf')
            if i == ROWS - 1:
                return matrix[i][j]
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            down = dfs(i + 1, j)
            left = dfs(i + 1, j - 1)
            right = dfs(i + 1, j + 1)
            
            memo[(i, j)] = matrix[i][j] + min(down, left, right)
            return memo[(i, j)]
        
        minim = float('inf')
        
        for j in range(COLS):
            minim = min(minim, dfs(0, j))
        
        return minim

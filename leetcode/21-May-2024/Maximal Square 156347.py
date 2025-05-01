# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        side = 0
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    if matrix[i][j] == "1":
                        dp[i][j] = 1
                else:
                    if matrix[i][j] == "1":
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                side = max(side, dp[i][j])
        
        return side * side
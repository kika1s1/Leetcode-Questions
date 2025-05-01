from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        R, C = len(board), len(board[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r, c):
            return 0 <= r < R and 0 <= c < C

        def dfs(r, c):
            if not inbound(r, c) or board[r][c] != "O":
                return
            board[r][c] = "#"  
            for dr, dc in direction:
                dfs(r + dr, c + dc)

        for i in range(R):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][C - 1] == "O":
                dfs(i, C - 1)
        for j in range(C):
            if board[0][j] == "O":
                dfs(0, j)
            if board[R - 1][j] == "O":
                dfs(R - 1, j)

        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

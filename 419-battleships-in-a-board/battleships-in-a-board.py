class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        R, C = len(board), len(board[0])
        directions = [(0, 1), (1, 0)]
        ans  = 0
        def inbound(r, c):
            return 0 <=r<R and 0 <=c<C
        def dfs(r, c):
            board[r][c] = "#"
            for x, y in directions:
                nr, nc = x + r, y + c
                if inbound(nr, nc) and board[nr][nc] == "X":
                    dfs(nr, nc)

        for i in range(R):
            for j in range(C):
                if board[i][j] == "X":
                    dfs(i, j)
                    ans +=1
        return ans


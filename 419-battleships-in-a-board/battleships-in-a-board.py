

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        R, C = len(board), len(board[0])
        directions = [(0, 1), (1, 0)]
        ans  = 0
        def inbound(r, c):
            return 0 <=r<R and 0 <=c<C

        for i in range(R):
            for j in range(C):
                if board[i][j] == "X":
                    # top
                    tr, tc = i-1, j
                    # row
                    rr, rc = i,  j-1
                    top =  inbound(tr, tc) and board[tr][tc] == "X"
                    row = inbound(rr, rc) and board[rr][rc] == "X"
                    if not (top or row):
                        ans +=1


        return ans


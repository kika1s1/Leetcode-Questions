class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for j in range(n)] for i in range(n)]
        cols,pos,neg = set(),set(),set()
        res = []

        def backtrack(r):
            if r==n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue

                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c]='Q'
                backtrack(r+1)
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                board[r][c]='.'

        backtrack(0)
        return res
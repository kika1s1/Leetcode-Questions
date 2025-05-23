class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = defaultdict(set)
        vertical = defaultdict(set)
        three_by_three = defaultdict(set)
        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                if board[i][j] ==".":
                    continue
                if board[i][j]  in horizontal[i]:
                    print("hh")
                    return False
                if board[i][j]  in vertical[j]:
                    return False
                if board[i][j] in three_by_three[(i//3, j//3)]:
                    return False
                horizontal[i].add(board[i][j])
                vertical[j].add(board[i][j])
                three_by_three[(i//3, j//3)].add(board[i][j])
                
        return True 
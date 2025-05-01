class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def inbound(r, c):
            return 0 <= r < 8 and 0 <= c < 8
        ans = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] =="R":
                    # right
                    r, c = i, j
                    while inbound(r,c):
                        
                        if board[r][c] == "B":
                            break
                        elif board[r][c] =="p":
                            ans +=1
                            break
                        r +=1
                    
                        
                    # left
                    r, c = i, j
                    while inbound(r,c):
                        if board[r][c] == "B":
                            break
                        elif board[r][c] =="p":
                            ans +=1
                            break
                        r -=1
                    
                    # up
                    r, c = i, j
                    while inbound(r,c):
                        if board[r][c] == "B":
                            break
                        elif board[r][c] =="p":
                            ans +=1
                            break
                        c -=1
                    
                    # down
                    r, c = i, j
                    while inbound(r,c):
                        if board[r][c] == "B":
                            break
                        elif board[r][c] =="p":
                            ans +=1
                            break
                        c +=1
        return ans
                    
                        
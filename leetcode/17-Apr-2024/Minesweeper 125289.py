# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board, click):

        if board[click[0]][click[1]] == 'M':      
            board[click[0]][click[1]] = 'X' ; return board  

        adjacent = lambda x,y : [(x+dx,y+dy) for dx in range(-1,2) for dy in range(-1,2) 
                if (dx or dy) and 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0])]
        
        def dfs(x: int,y: int)-> None:                     
            adj = adjacent(x,y)
                                                            
            mines = sum(board[X][Y] == 'M' for X,Y in adj)  
                                                            
            if  mines:
                board[x][y] = str(mines)                    

            else:    
                board[x][y] = 'B'                        

                for X,Y in adj:
                    if board[X][Y] == 'E':                 
                        dfs(X,Y)                            
            return                                        
                                                            
        dfs(*click)                                         

        return board                                        
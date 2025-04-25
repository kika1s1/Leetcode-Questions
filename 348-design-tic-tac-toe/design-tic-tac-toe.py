class TicTacToe:
    def __init__(self, n: int):
        self.row = defaultdict(list)
        self.cols = defaultdict(list)
        self.rev = []
        self.main = []
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        
        self.row[row].append(player)
        self.cols[col].append(player)
        if row == col:
            self.main.append(player)
        if (row + col)+1 == self.n:
            self.rev.append(player)
        
        if len(set(self.row[row])) == 1 and len(self.row[row]) == self.n:
            return player
        elif len(set(self.cols[col])) ==1 and len(self.cols[col]) == self.n:
            return player 
        elif len(set(self.main)) ==1 and len(self.main) == self.n:
            return player
        elif len(set(self.rev)) == 1 and len(self.rev) == self.n:
            return player
        
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
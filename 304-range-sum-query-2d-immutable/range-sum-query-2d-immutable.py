class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        self.matrix = [[0] * c for i in range(r)]
        self.old_matrix = matrix
        prev = 0
        for i in range(r):
            for j in range(c):
                prev += matrix[i][j]
                self.matrix[i][j] +=prev
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2+1):
            total +=(self.matrix[i][col2]-(self.matrix[i][col1])+self.old_matrix[i][col1])
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
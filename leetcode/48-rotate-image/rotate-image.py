class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            row = matrix[i]
            l, r = 0, len(row)-1
            while l <= r:
                row[l], row[r] = row[r], row[l]
                r -=1
                l +=1
        
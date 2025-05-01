class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        cnt_neg = 0
        minim = float("inf")
        R, C = len(matrix), len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j] < 0:
                    cnt_neg +=1
                total +=abs(matrix[i][j])
                minim =min(minim, abs(matrix[i][j]))
        if cnt_neg %2 == 1:
            total -=2 * minim
            return total
        return total

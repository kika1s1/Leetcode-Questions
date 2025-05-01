class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum(
            sum(mat[i][col] for i in range(len(mat))) == 1
            for col in [
                row.index(1)
                for row in mat
                if sum(row) == 1
            ]
        )
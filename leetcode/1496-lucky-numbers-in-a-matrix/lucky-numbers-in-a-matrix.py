class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        R, C = len(matrix), len(matrix[0])
        result = []

        min_row_values = [min(row) for row in matrix]

        for j in range(C):
            max_col_value = max(matrix[i][j] for i in range(R))
            if max_col_value in min_row_values:
                result.append(max_col_value)

        return result

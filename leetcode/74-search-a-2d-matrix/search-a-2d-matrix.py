class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R,  C = len(matrix), len(matrix[0])
        l,r =0,  R * C -1
        while l <=r:
            mid = (l+r)//2
            row = mid // C
            col = mid % C
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid-1
            else:
                l  = mid +1
        return False

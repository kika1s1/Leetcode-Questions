class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_90(matrix):
            R, C = len(matrix), len(matrix[0])
            rotated = []
            for i in range(C):
                col = []
                for j in range(R):
                    col.append(matrix[j][i])
                rotated.append(col[::-1])
            return rotated
        for i in range(4):
            if mat == target:
                return True
            mat = rotate_90(mat)
        return False
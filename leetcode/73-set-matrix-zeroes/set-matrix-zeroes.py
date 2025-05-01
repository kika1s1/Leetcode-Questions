class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        visited = set()
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0 and (i,j) not in visited:
                    for k in range(C):
                        if matrix[i][k] == 0:
                            continue
                        matrix[i][k] = 0
                        visited.add((i,k))
                    for a in range(R):
                        if matrix[a][j] == 0:
                            continue
                        matrix[a][j] = 0
                        visited.add((a,j))
                
        
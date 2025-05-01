class Solution(object):
    def transpose(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        ans = [[0]*r for _ in range(c)]
        for i in range(c):
            for j in range(r):
                ans[i][j] = matrix[j][i]

        return ans

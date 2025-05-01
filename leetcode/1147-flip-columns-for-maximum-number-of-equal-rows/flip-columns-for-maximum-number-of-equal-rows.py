class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        comes = defaultdict(int)
        R, C = len(matrix), len(matrix[0])
        for i in range(R):
            sub = []
            for j in range(C):
                sub.append(str(matrix[i][j]))
            comes["".join(sub)] +=1
        maxim = 0
        for sub in comes:
            op = []
            for bi in sub:
                if bi == "1":
                    op.append("0")
                else:
                    op.append("1")
            joined = "".join(op)
            if joined in comes:
                maxim = max(maxim, comes[joined]+comes[sub])
            else:
                maxim = max(maxim, comes[sub])

        return maxim
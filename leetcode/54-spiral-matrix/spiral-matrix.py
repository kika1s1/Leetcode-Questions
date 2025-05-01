class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        visited = set()
        queue = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        ans = []
        R, C = len(matrix), len(matrix[0])
        r, c, d = 0, 0, 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            visited.add((r, c))
            nr, nc = r + queue[d][0], c + queue[d][1]
            if not (0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited):
                d = (d + 1) % 4
                nr, nc = r + queue[d][0], c + queue[d][1]
            r, c = nr, nc
            

        return ans

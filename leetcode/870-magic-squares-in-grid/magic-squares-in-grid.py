class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0
        cnt = 0
        magic_sq = [
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        ]
        for r_start in range(n - 2):
            for c_start in range(m - 2):
                subgrid = [grid[r_start + i][c_start:c_start + 3] for i in range(3)]
                if subgrid in magic_sq:
                    cnt += 1
        return cnt
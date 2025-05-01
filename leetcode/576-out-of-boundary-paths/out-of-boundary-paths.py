class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        @cache
        def solve(moves, row, col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            if row - moves >= 0 and col - moves >= 0 and row + moves < m and col + moves < n:
                return 0
            return sum(solve(moves - 1, row + rd, col + cd) for rd, cd in directions)

        return solve(maxMove, startRow, startColumn) % (10**9 + 7)
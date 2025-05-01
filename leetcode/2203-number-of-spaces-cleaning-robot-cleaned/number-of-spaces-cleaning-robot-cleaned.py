class Solution:
    def numberOfCleanRooms(self, grid: List[List[int]]) -> int:
        directions = (0, 1, 0, -1, 0)
        R, C = len(grid), len(grid[0])
        cnt = 0

        r, c = 0, 0
        d = 0

        while not grid[r][c] >> (d + 1) & 1:
            if grid[r][c] == 0:
                cnt += 1

            grid[r][c] |= 1 << (d + 1)

            nr = r + directions[d]
            nc = c + directions[d + 1]
            if (
                0 <= nr < R
                and 0 <= nc < C
                and grid[nr][nc] != 1
            ):
                r = nr
                c = nc

            else:
                d = (d + 1) % 4

        return cnt

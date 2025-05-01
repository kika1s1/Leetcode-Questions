class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r, c])
        def out_bound(r, c):
            if r == ROWS or r < 0 or  c == COLS or c < 0 or grid[r][c] !=1 :
                return True
            return False
        directions = [(0, 1), (0,-1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc+c
                    if out_bound(row, col):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -=1
            time +=1
        return time if fresh ==0 else -1





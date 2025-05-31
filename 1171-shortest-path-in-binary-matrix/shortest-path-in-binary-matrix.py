class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1  

        while queue:
            row, col, dist = queue.popleft()

            if row == n - 1 and col == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1 
                    queue.append((nr, nc, dist + 1))

        return -1 

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1),(1, -1) ]
        R, C = len(grid), len(grid[0])
        def inbound(r, c):
            return 0 <=r <R and 0 <=c<C and grid[r][c] == 0
        if grid[0][0] == 1:
            return -1
        

        queue = deque([(0, 0, 1)])
        visited.add((0, 0))
        while queue:
            for _ in range(len(queue)):
                i, j, dist = queue.popleft()
                if i == R-1 and j == C-1:
                    return dist
                for xi, yj in directions:
                    nr, nc = xi+i, yj + j
                    if inbound(nr, nc) and (nr, nc) not in visited:
                        queue.append((nr, nc, dist+1))
                        visited.add((nr, nc))
        return -1            
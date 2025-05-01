class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def inbound(r, c):
            return 0 <= r < R and 0 <= c < C
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(r, c, node):
            cnt = 1
            grid[r][c] = node  
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                for i, j in directions:
                    nr, nc = i + x, j + y
                    if inbound(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = node  
                        stack.append((nr, nc))
                        cnt += 1
            return cnt

        size = defaultdict(int) 
        node = 2  
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    size[node] = dfs(i, j, node)
                    node += 1

        if not size:
            return 1
        
        maxim = max(size.values(), default=0)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    connected = set()
                    total = 1  
                    for r, c in directions:
                        nr, nc = r + i, c + j
                        if inbound(nr, nc) and grid[nr][nc] != 0:
                            connected.add(grid[nr][nc])
                    for island in connected:
                        total += size[island]
                    maxim = max(maxim, total)
        
        return maxim
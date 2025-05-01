class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  
        
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]  
        visited = [[False] * n for _ in range(m)]  
        
        while heap:
            time, row, col = heappop(heap)
            
            if row == m - 1 and col == n - 1:
                return time
            
            if visited[row][col]:
                continue
            visited[row][col] = True
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    if grid[r][c] <= time + 1:
                        heappush(heap, (time + 1, r, c))
                    else:
                        diff = grid[r][c] - time
                        if diff % 2 == 1:
                            heappush(heap, (grid[r][c], r, c))
                        else:
                            heappush(heap, (grid[r][c] + 1, r, c))
        
        return -1
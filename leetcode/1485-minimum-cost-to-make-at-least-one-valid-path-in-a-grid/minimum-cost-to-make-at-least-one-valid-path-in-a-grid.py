class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0 
        pq = [(0, 0, 0)]  
        while pq:
            current_cost, x, y = heappop(pq)
            if current_cost > cost[x][y]:
                continue
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = current_cost + (1 if grid[x][y] != i + 1 else 0)
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heappush(pq, (new_cost, nx, ny))
        return cost[m - 1][n - 1]

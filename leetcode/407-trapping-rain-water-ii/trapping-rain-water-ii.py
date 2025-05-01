class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        for i in range(m):
            for j in (0, n - 1):
                heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        for j in range(n):
            for i in (0, m - 1):
                heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        volume = 0

        while min_heap:
            height, x, y = heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    volume += max(0, height - heightMap[nx][ny])
                    heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))

        return volume

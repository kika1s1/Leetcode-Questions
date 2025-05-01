class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(grid), len(grid[0])
        
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        
        total_points = 0
        
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        res = [0] * len(queries)
        
        for query, index in sorted_queries:
            while heap and heap[0][0] < query:
                value, x, y = heappop(heap)
                total_points += 1
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited:
                        heappush(heap, (grid[nx][ny], nx, ny))
                        visited.add((nx, ny))
            
            res[index] = total_points
        
        return res


                
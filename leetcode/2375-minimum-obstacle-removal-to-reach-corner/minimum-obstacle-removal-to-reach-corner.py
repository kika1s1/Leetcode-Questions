class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        
        ROWS, COLS = len(grid), len(grid[0])
        distances = [[float("inf") for _ in range(COLS)] for _ in range(ROWS)]
        heap = [(0, (0, 0))]  # (distance, (row, col))
        distances[0][0] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while heap:
            distance, (row, col) = heapq.heappop(heap)
            if (row, col) == (ROWS - 1, COLS - 1):
                return distance
            
            if distance > distances[row][col]:
                continue 
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if inbound(new_row, new_col):
                    new_distance = distance + grid[new_row][new_col]
                    if new_distance < distances[new_row][new_col]:
                        distances[new_row][new_col] = new_distance
                        heapq.heappush(heap, (new_distance, (new_row, new_col)))
        
        return distances[ROWS - 1][COLS - 1]

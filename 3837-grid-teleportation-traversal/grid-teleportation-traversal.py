

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        R, C = len(matrix), len(matrix[0])
        grid = [list(row) for row in matrix]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        capitals = set(ascii_uppercase)

        # Build portal map
        portal_map = defaultdict(list)
        for i in range(R):
            for j in range(C):
                ch = grid[i][j]
                if ch in capitals:
                    portal_map[ch].append((i, j))

        # Dijkstra's setup
        heap = [(0, 0, 0)]  # (cost, i, j)
        dist = [[float('inf')] * C for _ in range(R)]
        dist[0][0] = 0
        used_portals = set()

        def inbound(i, j):
            return 0 <= i < R and 0 <= j < C and grid[i][j] != '#'

        while heap:
            cost, i, j = heapq.heappop(heap)

            if (i, j) == (R-1, C-1):
                return cost

            # Skip if we already have a better path
            if cost > dist[i][j]:
                continue

            # Try moving in 4 directions (cost 1)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if inbound(ni, nj) and cost + 1 < dist[ni][nj]:
                    dist[ni][nj] = cost + 1
                    heapq.heappush(heap, (cost + 1, ni, nj))

            # Try teleporting (cost 0)
            ch = grid[i][j]
            if ch in capitals and ch not in used_portals:
                for pi, pj in portal_map[ch]:
                    if cost < dist[pi][pj]:
                        dist[pi][pj] = cost
                        heapq.heappush(heap, (cost, pi, pj))
                used_portals.add(ch)

        return -1

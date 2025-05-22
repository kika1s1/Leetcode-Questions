from collections import deque, defaultdict
from string import ascii_uppercase
from typing import List

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        R, C = len(matrix), len(matrix[0])
        grid = [list(row) for row in matrix]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        capitals = set(ascii_uppercase)

        # 1) Build portal map
        portal_map = defaultdict(list)
        for i in range(R):
            for j in range(C):
                ch = grid[i][j]
                if ch in capitals:
                    portal_map[ch].append((i, j))

        # 2) Distance array (inf = unreachable)
        INF = 10**9
        dist = [[INF]*C for _ in range(R)]
        dist[0][0] = 0

        dq = deque([(0, 0)])
        used_portals = set()

        def inbound(i, j):
            return 0 <= i < R and 0 <= j < C and grid[i][j] != '#'

        # 3) 0–1 BFS loop
        while dq:
            i, j = dq.popleft()
            d = dist[i][j]

            # a) Teleportation (cost = 0)
            ch = grid[i][j]
            if ch in capitals and ch not in used_portals:
                for pi, pj in portal_map[ch]:
                    if d < dist[pi][pj]:
                        dist[pi][pj] = d
                        dq.appendleft((pi, pj))
                used_portals.add(ch)

            # b) Normal steps (cost = 1)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if inbound(ni, nj) and d + 1 < dist[ni][nj]:
                    dist[ni][nj] = d + 1
                    dq.append((ni, nj))

        # 4) Return answer (or -1 if unreachable)
        ans = dist[R-1][C-1]
        return ans if ans < INF else -1

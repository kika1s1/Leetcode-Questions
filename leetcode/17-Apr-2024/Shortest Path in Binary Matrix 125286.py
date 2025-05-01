# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from sys import maxsize
from heapq import heappush, heappop

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        length = [[maxsize for _ in range(n)] for _ in range(n)]
        offset = [(1,1),(1,0),(0,1),(-1,1),(1,-1),(-1,0),(0,-1),(-1,-1)]

        if grid[0][0] == 0 and grid[n-1][n-1] == 0:
            heap.append((n,0,0))
            length[0][0] = 1

        while heap:
            _, i, j = heappop(heap)
            L = length[i][j] + 1

            if (i,j) == (n-1,n-1):
                return L-1

            for di, dj in offset:
                x, y = i+di, j+dj
                if 0 <= x < n and 0 <= y n:
                    if grid[x][y] == 0 and length[x][y] > L:
                        length[x][y] = L
                        heappush(heap, (L+max(n-x, n-y), x, y))
        
        return -1
from typing import *
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4*n*n)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        for i in range(n):
            for j in range(n):
                base = 4*(i*n+j)
                if grid[i][j] == '/':
                    union(base+0, base+3)
                    union(base+1, base+2)
                elif grid[i][j] == '\\':
                    union(base+0, base+1)
                    union(base+2, base+3)
                else:
                    union(base+0, base+1)
                    union(base+1, base+2)
                    union(base+2, base+3)
                if i < n-1:
                    union(base+2, base+4*n+0)
                if j < n-1:
                    union(base+1, base+4+3)
        return sum(find(i) == i for i in range(4*n*n))
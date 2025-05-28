class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])
        def inbound(r, c):
            return 0 <=r <R and 0 <=c < C and grid[r][c] !=-1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        obstacles = 0
        x, y = 0, 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == -1:
                    obstacles +=1
                if grid[i][j] == 1:
                    x = i
                    y = j
                    

        def backtrack(r, c, visited):
            nonlocal ans
            if grid[r][c] == 2:
                # print(len(visited))
                if len(visited) == (R*C - obstacles):
                    ans +=1
                    return
                return 
            for x, y in directions:
                nr, nc = x+r, y+c
                if inbound(nr, nc) and (nr, nc) not in visited:
                    visited.append((nr, nc))
                    backtrack(nr, nc, visited)
                    visited.pop()
            return ans


        return backtrack(x, y, [(x, y)])
                     

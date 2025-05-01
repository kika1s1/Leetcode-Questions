class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def order(conditions):
            adj = [[] for _ in range(k + 1)]
            deg = [0] * (k + 1)
            for u, v in conditions:
                adj[u].append(v)
                deg[v] += 1

            s = []
            for u, d in enumerate(deg):
                if u and d == 0:
                    s.append(u)
            
            res = []
            while s:
                u = s.pop()
                res.append(u)
                for v in adj[u]:
                    deg[v] -= 1
                    if deg[v]:
                        continue
                    s.append(v)

            if any(deg):
                return []
            return res

            
        row = order(rowConditions)
        col = order(colConditions)
        
        col = {x: i for i, x in enumerate(col)}
        res = [[0] * k for _ in range(k)]
        for i, x in enumerate(row):
            if x not in col:
                break
            j = col[x]
            res[i][j] = x

        for r in res:
            if not any(r):
                return []
        return res
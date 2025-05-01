
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.minim = [-1] * n  

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x,y, w):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            self.minim[rootX] &= w
            return
        new_min = self.minim[rootX] & self.minim[rootY] & w
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.minim[rootX] = new_min
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            self.minim[rootY] = new_min
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
            self.minim[rootX] = new_min

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for x, y, w in edges:
            uf.union(x, y, w)
        
        ans = []
        for s, e in queries:
            if uf.find(s) == uf.find(e):
                ans.append(uf.minim[uf.find(s)])
            else:
                ans.append(-1)
        return ans

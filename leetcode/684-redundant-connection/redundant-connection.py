class UnionFind:
    def __init__(self, n):
        self.parent = {x:x for x in range(1, n+1)}
        self.rank = {x:0 for x in range(1, n+1)}
    def find(self, x):
        if x !=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] +=1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
            
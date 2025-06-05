class UnionFind:
    def __init__(self):
        self.parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if root_u < root_v:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for a, b in zip(s1, s2):
            uf.union(a, b)
        return ''.join(uf.find(c) for c in baseStr)

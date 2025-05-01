class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.connected = [0 for i in range(n)]
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        self.connected[u] +=1
        self.connected[v] +=1
        if rootV == rootU:
            return 
        if self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = self.parent[rootU]
        elif self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = self.parent[rootV]
        else:
            self.parent[rootV] = self.parent[rootU]
            self.rank[rootU]  +=1


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        components = defaultdict(list)
        for index, node in enumerate(uf.parent):
            components[uf.find(node)].append(index)
        cnt = 0
        for key in components:
            is_connected = True
            for i in range(1, len(components[key])):
                if uf.connected[components[key][i-1]]  != len(components[key])-1:
                    is_connected = False
            if is_connected:
                cnt +=1
        return cnt

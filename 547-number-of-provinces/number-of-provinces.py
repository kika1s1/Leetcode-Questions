class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        p_u = self.find(u)
        p_v = self.find(v)
        if p_u == p_v:
            return False
        if self.rank[p_u] > self.rank[p_v]:
            self.parent[p_v] = p_u
        elif self.rank[p_u] < self.rank[p_v]:
            self.parent[p_u] = p_v
        else:
            self.parent[p_v] = p_u
            self.rank[p_u] += 1
        return True  

    

class Solution:
    def findCircleNum(self, isConnected):
        N = len(isConnected)
        un = UnionFind(N)
        count = N
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] and un.union(i, j):
                    count -= 1
        return count

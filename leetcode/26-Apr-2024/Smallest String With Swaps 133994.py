# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        uf = UnionFind(N)
        for a, b in pairs:
            uf.union(a, b)
        groups_i = defaultdict(list)
        groups_ch = defaultdict(list)
        for i in range(N):
            group = uf.find(i)
            groups_i[group].append(i)
            groups_ch[group].append(s[i])
        
        res = [""]*N
        for g in groups_i.keys():
            indx = sorted(groups_i[g])
            chrs = sorted(groups_ch[g])
            for i, ch in zip(indx, chrs):
                res[i] +=ch
        return "".join(res)


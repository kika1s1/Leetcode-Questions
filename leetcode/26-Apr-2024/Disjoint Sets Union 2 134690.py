# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def get(self,x):
        ele = self.find(x)
        minim, maxim = float("inf"), float("-inf")
        cnt = 0
        for i in range(1, len(self.parent)):
            if self.find(i) == ele:
                cnt += 1
                minim = min(minim, i)
                maxim = max(maxim, i)
        return minim, maxim, cnt


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
n, q = map(int, input().split())
uf = UnionFind(n)
for i in range(q):
    query = list(map(str, input().split()))
    if query[0] == "union":
        uf.union(int(query[1]), int(query[2]))
    else:
        print(*uf.get(int(query[1])))

    
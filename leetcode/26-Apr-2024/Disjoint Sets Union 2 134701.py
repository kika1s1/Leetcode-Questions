# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.size = [1] * (size + 1)
        self.min = list(range(size + 1))
        self.max = list(range(size + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def get(self, x):
        parent = self.find(x)
        return [self.min[parent], self.max[parent], self.size[parent]]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]
            self.min[rooty] = min(self.min[rootx], self.min[rooty])
            self.max[rooty] = max(self.max[rootx], self.max[rooty])


n, q = map(int, input().split())
uf = UnionFind(n)
for _ in range(q):
    cmd = list(map(str, input().split()))
    if cmd[0] == "union":
        uf.union(int(cmd[1]), int(cmd[2]))
    else:
        result = uf.get(int(cmd[1]))
        print(result[0], result[1], result[2])
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)

        def find(x):
            if parent[x]!=x:
                return find(parent[x])

            return x

        def union(a, b):
            if a!=b:
                parent[find(a)]=find(b)
            
        for i, j in stones:
            parent[(i,j)] = (i, j)
            row[i].append((i, j))
            col[j].append((i, j))
        
        for i in row:
            for x in row[i]:
                union(row[i][0], x)
        for j in col:
            for x in col[j]:
                union(col[j][0], x)
        
        unions = set(find((i, j)) for i , j in stones)
        return len(stones)-len(unions)
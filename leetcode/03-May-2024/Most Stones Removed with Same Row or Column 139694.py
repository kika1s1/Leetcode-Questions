# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        hash_row = defaultdict(list)
        hash_col = defaultdict(list)
        
        parent =  {}
        for i,stone in enumerate(stones):
            x,y= stone[0],stone[1]
            hash_row[x].append((x,y))
            hash_col[y].append((x,y))
            stones[i]= tuple(stone)
            parent[tuple(stone)]= tuple(stone)
        
        def find(x,y):
            if parent[(x,y)]!=(x,y):
                parent[(x,y)]=find(parent[(x,y)][0],parent[(x,y)][1])
            return parent[(x,y)]

        def union(x_1,y_1,x_2,y_2):
            r1= find(x_1,y_1)
            r2 = find(x_2,y_2)
            if r1!=r2:
                parent[r1]=r2
        for row in hash_row.keys():
            row = hash_row[row]
            p1 = row[0]
            for p2 in row[1:]:
                union(p1[0],p1[1],p2[0],p2[1])
        for col in hash_col.keys():
            col = hash_col[col]
            p1 = col[0]
            for p2 in col[1:]:
                union(p1[0],p1[1],p2[0],p2[1])
        group = set()                
        for point in parent.keys():
            cluster_root = find(point[0],point[1])
            group.add(cluster_root)
        return len(stones)-len(group)
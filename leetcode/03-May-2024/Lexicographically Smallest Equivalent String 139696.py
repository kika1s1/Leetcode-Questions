# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # union find by Rank 

        parent = {a : a for a in s1 + s2}
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        for a, b in zip(s1, s2):
            union(a, b)
        ans = ""
        for s in baseStr:
            if s in parent:
                ans += find(s)
            else:
                ans += s
        return ans

        
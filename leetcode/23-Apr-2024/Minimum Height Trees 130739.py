# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [i for i in range(n)]
            
        graph = defaultdict(set)

        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = []
        for i in range(n):
            if len(graph[i])==1:
                leaves.append(i)

        remaining = n
        while remaining>2:
            remaining-=len(leaves)
            newLeaves = []
            while leaves:
                leaf = leaves.pop()
                nei = graph[leaf].pop()
                graph[nei].remove(leaf)
                if len(graph[nei])==1:
                    newLeaves.append(nei)

            leaves = newLeaves[:]

        return leaves
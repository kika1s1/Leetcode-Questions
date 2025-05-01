# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            if n == 1:
                return 0
            else:
                return -1
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        def dfs(graph, visited, node):
            visited.add(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    dfs(graph, visited, neighbour)
        
        for u, v in edges:
            visited = set()
            dfs(graph, visited, u)
            if len(visited) == n:
                return u
        
        return -1
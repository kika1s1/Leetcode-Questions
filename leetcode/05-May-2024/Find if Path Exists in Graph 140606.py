# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges and destination == 0:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(graph, source, destination, visited):
            stack =[source]
            while stack:
                node = stack.pop()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        if neighbour == destination:
                            return True
                        stack.append(neighbour)
            return False
        return bfs(graph, source, destination, set())
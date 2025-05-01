# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph_so_far = defaultdict(list)
        def path_exists(u, v):
            if u == v:
                return True
            visited.add(u)
            for neighbor in graph_so_far[u]:
                if neighbor not in visited:
                    if path_exists(neighbor, v):
                        return True
            return False

        for u, v in edges:
            visited = set()
            if path_exists(u,v):
                return [u,v]
            else:
                graph_so_far[u].append(v)
                graph_so_far[v].append(u)

        return None
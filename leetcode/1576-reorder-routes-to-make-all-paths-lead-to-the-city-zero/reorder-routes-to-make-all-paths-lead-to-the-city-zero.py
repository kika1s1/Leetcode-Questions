class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        reorder_count = 0
        visited = set()

        for a, b in connections:
            graph[a].append((b, 1))  
            graph[b].append((a, 0)) 
        # print(graph)

        def dfs(node):
            nonlocal reorder_count
            visited.add(node)

            for neighbor, direction in graph[node]:
                if neighbor not in visited:
                    reorder_count += direction  
                    dfs(neighbor)

        dfs(0) 
        return reorder_count
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        def dfs(visited, current):
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    dfs(visited, neighbor)

        ans = []
        for node in range(n):
            visited = set()
            dfs(visited, node)
            if len(visited) == n:
                ans.append(node)

        if len(ans) == 1:
            return ans[0]
        return -1
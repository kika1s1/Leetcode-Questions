class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        stack = [source]
        visited = set([source])
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        return False
        # visited = set()
        # def dfs(node):
        #     if node == destination:
        #         return True
        #     visited.add(node)
        #     for nei in graph[node]:
        #         if nei not in visited:
        #             if dfs(nei): 
        #                 return True
        #     return False 
        # return dfs(source)
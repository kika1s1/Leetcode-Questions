class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        N = len(edges)
        for key in graph:
            if len(graph[key]) == N:
                return key
        return -1
        


    
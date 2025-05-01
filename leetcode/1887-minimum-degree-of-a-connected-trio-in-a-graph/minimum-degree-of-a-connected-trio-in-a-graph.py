class Solution:
    def minTrioDegree(self, n: int, edges: list[list[int]]) -> int:
        
        graph = defaultdict(set)
        degrees = [0] * (n + 1)
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degrees[u] += 1
            degrees[v] += 1
        
        min_degree = float('inf')
        
        for u in range(1, n + 1):
            for v in graph[u]:  
                if v > u:  
                    for w in graph[u].intersection(graph[v]):  # Common neighbors
                        if w > v:  
                            degree = (degrees[u] + degrees[v] + degrees[w] - 6)
                            min_degree = min(min_degree, degree)
        
        return min_degree if min_degree != float('inf') else -1

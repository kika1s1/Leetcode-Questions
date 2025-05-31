
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    product = dfs(neighbor, end, visited)
                    if product != -1.0:
                        return product * value
            
            visited.remove(start)
            return -1.0
        
        results = []
        
        for dividend, divisor in queries:
            if dividend in graph and divisor in graph:
                result = dfs(dividend, divisor, set())
            else:
                result = -1.0
            results.append(result)
        
        return results


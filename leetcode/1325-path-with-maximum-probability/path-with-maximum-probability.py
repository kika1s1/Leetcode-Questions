class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        def dijkstra(graph, start):
            dist = {node: 0 for node in graph}
            heap = [(-1.0, start)]
            dist[start] = 1
            while heap:
                prob, node = heapq.heappop(heap)
                prob = -prob
                for neighbor, weight in graph[node].items():
                    new_prob = prob * weight
                    if new_prob > dist[neighbor]:
                        dist[neighbor] = new_prob
                        heapq.heappush(heap, (-new_prob, neighbor))

            return dist
        graph = {i: {} for i in range(n)}
        for i, (u, v) in enumerate(edges):
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]
        return dijkstra(graph, start_node)[end_node]
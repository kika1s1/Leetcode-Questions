class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(graph, source):
            distances = {node:float("inf") for node in range(1, n+1)}
            distances[source] = 0
            processed = set()
            heap = [(0,source)]
            while heap:
                distance, curr = heappop(heap)
                if curr in processed:
                    continue
                processed.add(curr)
                for child, weight in graph[curr]:
                    dist = weight + distance
                    if dist < distances[child]:
                        distances[child] = dist
                        heappush(heap, (dist, child))
            return distances
        graph = defaultdict(list)
        for u, v, w in times:
            if u not in graph:
                graph[u] = [(v,w)]
            else:
                graph[u].append((v,w))
            
        dist = max(dijkstra(graph, k).values())
        return dist if dist < float("inf") else -1




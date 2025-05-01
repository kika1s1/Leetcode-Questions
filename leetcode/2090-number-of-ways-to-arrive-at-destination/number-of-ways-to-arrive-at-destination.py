class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7 
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        min_heap = [(0, 0)]  
        shortest = [float('inf')] * n
        shortest[0] = 0
        ways = [0] * n  
        ways[0] = 1
        while min_heap:
            dist, node = heappop(min_heap)
            if dist > shortest[node]:
                continue
            for nei, time in graph[node]:
                new_dist = dist + time
                if new_dist < shortest[nei]:  
                    shortest[nei] = new_dist
                    heappush(min_heap, (new_dist, nei))
                    ways[nei] = ways[node]  
                elif new_dist == shortest[nei]:  
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        return ways[n-1]

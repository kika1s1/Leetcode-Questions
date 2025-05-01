class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        maxim_longest = -1
        for i in range(n):
            if not visited[i]:
                curr = i
                dist = {}
                cnt = 0
                while not visited[curr] and  curr != -1 and curr not in dist:
                    dist[curr] = cnt
                    visited[curr] = True
                    cnt += 1
                    curr = edges[curr]
                if curr != -1 and curr in dist:
                    long_cycle = cnt - dist[curr]
                    maxim_longest = max(maxim_longest, long_cycle)
        return maxim_longest

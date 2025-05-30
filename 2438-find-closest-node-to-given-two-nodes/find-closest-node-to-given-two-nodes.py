class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start: int):
            dist = [-1] * len(edges)
            queue = deque([start])
            dist[start] = 0
            while queue:
                curr = queue.popleft()
                neighbor = edges[curr]
                if neighbor != -1 and dist[neighbor] == -1:
                    dist[neighbor] = dist[curr] + 1
                    queue.append(neighbor)
            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        min_dist = float('inf')
        result = -1
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i
        return result

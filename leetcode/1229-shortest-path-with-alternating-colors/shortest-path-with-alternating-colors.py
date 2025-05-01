class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for s, d in redEdges:
            red[s].append(d)
        for s, d in blueEdges:
            blue[s].append(d)
        c_map = [red, blue]

        bfs = []
        visited = set()
        if 0 in red:
            bfs.append((0,1,0))
            visited.add((1,0))
        if 0 in blue:
            bfs.append((0,0,0))
            visited.add((0,0))

        result = defaultdict(int)
        result[0] = 0
        while bfs:
            dist, color, node = bfs.pop(0)
            if node not in result:  result[node] = dist
            next_color = int(not color)
            for next_node in c_map[next_color][node]:
                next_entry = (dist+1, next_color, next_node)
                visited_entry = (next_color, next_node)
                if visited_entry in visited:   continue
                visited.add(visited_entry)
                bfs.append(next_entry)
        return [result[i] if i in result else -1 for i in range(n)]
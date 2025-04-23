class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        incoming_edges = [0] * len(graph)
        adj_graph = defaultdict(list)
        for index, edges in enumerate(graph):
            incoming_edges[index] +=len(edges)
            for edge in edges:
                adj_graph[edge].append(index)

        ans = []
        queue = deque()
        for index, n_incoming in enumerate(incoming_edges):
            if n_incoming == 0:
                queue.append(index)
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in adj_graph[node]:
                incoming_edges[nei] -=1
                if incoming_edges[nei] == 0:
                    queue.append(nei)
        return sorted(ans)

            



"""
deque([5, 6])
defaultdict(<class 'list'>, {0: [1, 2], 1: [2, 3], 2: [5], 3: [0], 4: [5]})
"""
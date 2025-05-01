class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n

    def find(self, node):
        while self.parent[node] != -1:
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1

class Solution:
    def magnificentSets(self, n, edges):
        adj_list = [[] for _ in range(n)]
        uf = UnionFind(n)

        for u, v in edges:
            adj_list[u - 1].append(v - 1)
            adj_list[v - 1].append(u - 1)
            uf.union(u - 1, v - 1)

        num_of_groups_for_component = {}

        for node in range(n):
            number_of_groups = self._get_number_of_groups(adj_list, node, n)
            if number_of_groups == -1:
                return -1
            root_node = uf.find(node)
            num_of_groups_for_component[root_node] = max(
                num_of_groups_for_component.get(root_node, 0), number_of_groups
            )

        total_number_of_groups = sum(num_of_groups_for_component.values())
        return total_number_of_groups

    def _get_number_of_groups(self, adj_list, src_node, n):
        nodes_queue = deque()
        layer_seen = [-1] * n
        nodes_queue.append(src_node)
        layer_seen[src_node] = 0
        deepest_layer = 0

        while nodes_queue:
            num_of_nodes_in_layer = len(nodes_queue)
            for _ in range(num_of_nodes_in_layer):
                current_node = nodes_queue.popleft()
                for neighbor in adj_list[current_node]:
                    if layer_seen[neighbor] == -1:
                        layer_seen[neighbor] = deepest_layer + 1
                        nodes_queue.append(neighbor)
                    else:
                        if layer_seen[neighbor] == deepest_layer:
                            return -1
            deepest_layer += 1
        return deepest_layer
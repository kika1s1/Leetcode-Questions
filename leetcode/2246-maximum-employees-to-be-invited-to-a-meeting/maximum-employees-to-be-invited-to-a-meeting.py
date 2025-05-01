class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n
        for i in range(n):
            in_degree[favorite[i]] += 1

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        chain_length = [0] * n
        while queue:
            node = queue.popleft()
            neighbor = favorite[node]
            chain_length[neighbor] = chain_length[node] + 1
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

        visited = [False] * n
        cycle_lengths = []

        def calculate_cycle_length(node):
            cycle_size = 0
            current = node
            while not visited[current]:
                visited[current] = True
                current = favorite[current]
                cycle_size += 1
            return cycle_size

        for i in range(n):
            if in_degree[i] > 0 and not visited[i]:
                cycle_lengths.append(calculate_cycle_length(i))

        mutual_favorites_sum = 0
        for i in range(n):
            if favorite[favorite[i]] == i and i < favorite[i]:
                mutual_favorites_sum += 2 + chain_length[i] + chain_length[favorite[i]]

        return max(max(cycle_lengths, default=0), mutual_favorites_sum)

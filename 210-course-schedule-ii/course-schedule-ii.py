class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming_edge = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            incoming_edge[u] +=1
        queue = deque()
        for index, income_edge in enumerate(incoming_edge):
            if income_edge == 0:
                queue.append(index)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                incoming_edge[nei] -=1
                if incoming_edge[nei]  == 0:
                    queue.append(nei)
        if len(order) == numCourses:
            return order
        return []
    



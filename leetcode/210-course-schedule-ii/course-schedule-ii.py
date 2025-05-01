class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        0 => 1

        """
        graph = defaultdict(list)
        indegree  = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] +=1
        queue = deque([node for node, indeg in enumerate(indegree) if indeg == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        return order if numCourses == len(order) else []



            
        
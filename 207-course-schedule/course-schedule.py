class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        incoming_edge = [0] * numCourses
        graph  = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming_edge[course] +=1

        queue = deque()
        for index in range(numCourses):
            if incoming_edge[index] == 0:
                queue.append(index)
        visited = set()

        while queue:
            node = queue.popleft()
            visited.add(node)
            for nei in graph[node]:
                incoming_edge[nei]-=1
                if nei not in visited and incoming_edge[nei] ==0:
                    queue.append(nei)

        return len(visited) == numCourses
        


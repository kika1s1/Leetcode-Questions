class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        incoming = [0 for i in range(numCourses)]
        queue = deque()
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] +=1
        queue = deque()
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        order = []
        while queue:
            preq = queue.popleft()
            order.append(preq)
            for course in graph[preq]:
                incoming[course] -=1
                if  incoming[course] == 0:
                    queue.append(course)
        if len(order) != numCourses:
            return False
        return True
                
# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0 for i in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] +=1
        queue = deque()
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbour in graph[course]:
                incoming[neighbour] -=1
                if incoming[neighbour] == 0:
                    queue.append(neighbour)
        if len(order) != numCourses:
            return []
        return order


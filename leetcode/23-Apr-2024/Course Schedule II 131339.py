# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        
        for prerequisite in prerequisites:
            course, prerequisite_course = prerequisite
            graph[prerequisite_course].append(course)
            in_degrees[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if in_degrees[course] == 0:
                queue.append(course)
        
        order = []
        while queue:
            prerequisite_course = queue.popleft()
            order.append(prerequisite_course)
            
            for course in graph[prerequisite_course]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    queue.append(course)
        
        if len(order) != numCourses:
            return []
        
        return order
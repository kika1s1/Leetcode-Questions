# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for pre, course in prerequisites:
            graph[pre].append(course)

        ans = []
        for pre, course in queries:
            if self.isPrerequisite(pre, course, graph):
                ans.append(True)
            else:
                ans.append(False)

        return ans

    def isPrerequisite(self, source: int, target: int, adj_list: dict) -> bool:
        queue = deque([source])
        visited = set()

        while queue:
            curr = queue.popleft()
            if curr == target:
                return True

            visited.add(curr)
            for neighbor in adj_list[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False
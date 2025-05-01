# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for neighbour in graph[i]:
                if not dfs(neighbour):

                    return False
            safe[i] = True
            return True
        ans =[]
        for i in range( n):
            if dfs(i):
                ans.append(i)
        return ans
# Problem: IPO - https://leetcode.com/problems/ipo/


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]

        projects.sort(key=lambda x: x[0])
        print(projects)
        available = []
        i = 0

        while k > 0:
            while i < n and projects[i][0] <= w:
                heapq.heappush(available, -projects[i][1]) 
                i += 1

            if not available:
                break

            w -= heapq.heappop(available)
            k -= 1

        return w
# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
        

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
        
            for ch in graph[node]:
                dfs(ch)
            
        seen = set()
        res = 0
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                res += 1
        
        return res
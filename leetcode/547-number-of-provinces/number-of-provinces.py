class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph  = defaultdict(list)
        visited = [0 for i in range(len(isConnected)+1)]
        R = len(isConnected)
        for i in range(R):
            for j in range(R):
                if isConnected[i][j]:
                    graph[i+1].append(j+1)

        def dfs(node, seen):
            visited[node] = 1
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei, seen)
        cnt = 0
        for i in range(1, len(visited)):
            if visited[i] == 0:
                seen = set()
                dfs(i, seen)
                cnt +=1
        return cnt
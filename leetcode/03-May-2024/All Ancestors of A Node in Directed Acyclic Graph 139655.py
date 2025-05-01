# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] +=1
        
        d = deque([node for node in range(n) if node not in in_degree])
        res = [set() for _ in range(n)]
        while d:
            node = d.popleft()
            for child in graph[node]:
                res[child].add(node)
                res[child].update(res[node])
                in_degree[child] -=1
                if in_degree[child] == 0:
                    d.append(child)
        return [sorted(x) for x in res] 
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in trust:
            graph[a].append(b)
        for i in range(1, n+1):
            if i not in graph:
                all_trust = True
                for j in range(1,n+1):
                    if j !=i and (j not in graph or   i not in graph[j]):
                        all_trust = False
                        break
                if all_trust:
                    return i

        return -1
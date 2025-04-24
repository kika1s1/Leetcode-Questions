class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph  = defaultdict(list)
        ans  =[None for i in range(len(quiet))]
        for a, b in richer:
            graph[b].append(a)
        def dfs(node):
            if ans[node] is None:
                ans[node] = node
                for nei in graph[node]:
                    cand = dfs(nei)
                    if quiet[cand] < quiet[ans[node]]:
                        ans[node] = cand
            return ans[node]
        for node in range(len(quiet)):
            dfs(node)
        return ans
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph  = defaultdict(list)
        ans  =[i for i in range(len(quiet))]
        for a, b in richer:
            graph[b].append(a)
        @cache
        def dfs(node, index):
            ans[index] = node if quiet[ans[index]] > quiet[node]  else ans[index]
            for nei in graph[node]:
                dfs(nei, index)
        for node in range(len(quiet)):
            dfs(node, node)
        return ans
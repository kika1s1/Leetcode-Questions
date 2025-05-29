class Solution:
    def maxTargetNodes(self, e1: List[List[int]], e2: List[List[int]]) -> List[int]:
        def dfs(u, p, d, g, col):
            col[u] = d % 2
            cnt = 1 - col[u]
            for v in g[u]:
                if v != p:
                    cnt += dfs(v, u, d + 1, g, col)
            return cnt

        def countColors(edges, col):
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            c0 = dfs(0, -1, 0, g, col)
            return [c0, len(edges) + 1 - c0]

        n = len(e1) + 1
        m = len(e2) + 1
        col1 = [0] * n
        col2 = [0] * m
        cnt1 = countColors(e1, col1)
        cnt2 = countColors(e2, col2)

        ans = [0] * n
        for i in range(n):
            ans[i] = cnt1[col1[i]] + max(cnt2)
        return ans

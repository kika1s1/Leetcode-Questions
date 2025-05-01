# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E


def dfs(u):
    global isCycle
    stack = [u]
    while stack:
        curr = stack.pop()
        vis[curr] = True
        if len(adj[curr]) != 2:
            isCycle = False
        for v in adj[curr]:
            if not vis[v]:
                stack.append(v)

n, m = map(int, input().split())
global adj, vis, isCycle
adj = [[] for _ in range(n+1)]
vis = [False] * (n+1)
isCycle = True

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

ans = 0
for i in range(1, n+1):
    if not vis[i]:
        isCycle = True
        dfs(i)
        if isCycle:
            ans += 1

print(ans)

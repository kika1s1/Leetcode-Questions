# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        def dfs(node, parent=None):
            if not node:
                return
            if parent:
                adj[node.val].append(parent.val)
            if node.left:
                adj[node.val].append(node.left.val)
                dfs(node.left, node)
            if node.right:
                adj[node.val].append(node.right.val)
                dfs(node.right, node)
        dfs(root)
                
        q = deque([(target.val, k)])
        visited = set()
        visited.add(target.val)
        ans = []
        while q:
            for _ in range(len(q)):
                nd, dist = q.popleft()
                if dist == 0:
                    ans.append(nd)
                else:
                    for ng in adj[nd]:
                        if not ng in visited:
                            visited.add(ng)
                            q.append((ng, dist-1))
        return ans
                

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, mx, mn):
            nonlocal res
            if not node: 
                return
            
            mx = max(node.val, mx)
            mn = min(node.val, mn)
            res = max(abs(mx-mn), res)
            dfs(node.left, mx, mn)
            dfs(node.right, mx, mn)
        dfs(root.left, root.val, root.val)
        dfs(root.right, root.val, root.val)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node , mx ):
            nonlocal cnt
            if not node:
                return
            if mx <= node.val:
                cnt += 1
            mx = max(mx, node.val)
            
            if node.right:
                dfs(node.right,mx)
            if node.left:
                dfs(node.left, mx)
        dfs(root,root.val)
        return cnt
    
    
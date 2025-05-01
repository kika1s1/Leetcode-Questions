# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(root, added):
            nonlocal total
            if not root:
                return 
            if not root.left and not root.right:
                total += added
            if root.left:
                dfs(root.left, added*10+root.left.val)
            if root.right:
                dfs(root.right, added*10+root.right.val)
            return total
        return dfs(root, root.val)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(first, second):
            if not first and not second:
                return True
            if not first or not second:
                return False
            return first.val == second.val and dfs(first.left, second.left) and dfs(first.right, second.right)
        return dfs(p, q)
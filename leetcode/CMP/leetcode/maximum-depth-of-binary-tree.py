# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root, dep):
            if root is None:
                return dep
            else:
                return max(depth(root.left, dep+1), depth(root.right, dep+1))
        return depth(root, 0)
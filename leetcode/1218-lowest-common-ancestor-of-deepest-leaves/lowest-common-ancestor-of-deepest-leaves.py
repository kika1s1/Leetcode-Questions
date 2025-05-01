# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(current_node):
            if not current_node:
                return (0, None)
            left_depth, left_lca = dfs(current_node.left)
            right_depth, right_lca = dfs(current_node.right)
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif left_depth < right_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth +1, current_node)

        return dfs(root)[1]
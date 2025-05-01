# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        def traverse(current_node, results):
            if current_node is None:
                return 
            results.append(current_node.val)
            if current_node.left is not None:
                traverse(current_node.left, results)
            if current_node.right is not None:
                traverse(current_node.right, results)
        traverse(root,results)
        results.sort()
        return results[k-1]
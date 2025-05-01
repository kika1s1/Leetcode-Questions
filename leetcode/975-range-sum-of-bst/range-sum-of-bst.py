# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = [0]  # Use a mutable object, like a list, for total

        def preorder(root, total, low, high):
            if root.val >= low and root.val <= high:
                total[0] += root.val
            if root.left is not None:
                preorder(root.left, total, low, high)
            if root.right is not None:
                preorder(root.right, total, low, high)
        
        preorder(root, total, low, high)
        return total[0]
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def isValidBST(self, root: Optional[TreeNode]) -> bool:
        previous = -float("inf")
        result = True

        def inorder(node):
            nonlocal previous, result
            if not node or not result:
                return

            inorder(node.left)
            if previous >= node.val:
                result = False
                return

            previous = node.val
            inorder(node.right)

        inorder(root)
        return result
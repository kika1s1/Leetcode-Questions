# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global count, result
        count = 0  # Initialize global count
        result = None  # Global variable to store the k-th smallest element

        def inorder(node):
            global count, result
            if not node or result is not None:  # Stop early if k-th element found
                return

            inorder(node.left)  # Visit left subtree

            count += 1
            if count == k:  # If k-th smallest is found
                result = node.val
                return

            inorder(node.right)  # Visit right subtree
        
        inorder(root)
        return result
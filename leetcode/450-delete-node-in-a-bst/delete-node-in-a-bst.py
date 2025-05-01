# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def min_val(root):
            current = root
            while current.left:
                current = current.left
            return current
        def deleteNode(root, key):
            if not root:
                return root
            if root.val > key:
                root.left = deleteNode(root.left, key)
            elif root.val < key:
                root.right = deleteNode(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    temp = min_val(root.right)
                    root.val = temp.val
                    root.right = deleteNode(root.right, temp.val)
            return root
        return deleteNode(root, key)
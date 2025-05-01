# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val=val)
        # if root is None:
        #     root = new_node
        #     return root
        # temp = root
        # while True:
        #     if new_node.val < temp.val:
        #         if temp.left is None:
        #             temp.left = new_node
        #             return root
        #         temp = temp.left
        #     else:
        #         if temp.right is None:
        #             temp.right = new_node
        #             return root
        #         temp =temp.right
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root
        self.insertIntoBST(root, val)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return 
        data = preorder[0]
        root = TreeNode(data)
        low = [i for i in preorder if i < data]
        high = [i for i in preorder if i > data]
        root.left = self.bstFromPreorder(low)
        root.right = self.bstFromPreorder(high)
        return root
        
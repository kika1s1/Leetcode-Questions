# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def transverse(current_node):
            if current_node is None:
                return 
            if current_node.left is not None:
                transverse(current_node.left)
            ans.append(current_node.val)
            if current_node.right is not None:
                transverse(current_node.right)
        transverse(root)
        return ans
                
        
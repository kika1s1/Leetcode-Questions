# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -float('inf')
        minim = float('inf')
        
        def in_order(node: Optional[TreeNode]):
            nonlocal prev, minim
            if not node:
                return
            
            in_order(node.left)
            
            minim = min(minim, node.val - prev)
            prev = node.val
            
            in_order(node.right)
        
        in_order(root)
        return minim
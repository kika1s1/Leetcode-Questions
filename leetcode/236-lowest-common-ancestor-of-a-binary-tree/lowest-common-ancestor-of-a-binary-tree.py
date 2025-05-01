# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node): 
            if node == None: 
                return None
            if node == p or node == q:
                return node
            left = traverse(node.left) 
            right = traverse(node.right)
            if left and right: 
                return node
            return left or right 
        return traverse(root)
            
            
            
        
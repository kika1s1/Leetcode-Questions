# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        cases when the right child of the current tree is null and 
        when the left child of the current tree is null
        when both the childs are none
        
        '''

        # recursion 
        def dfs(flip, target):
            if not flip and not target:
                return True
            elif not flip:
                return False
            elif not target:
                return False
            
            if flip.val != target.val:
                return False

            correct = dfs(flip.left, target.left) and dfs(flip.right, target.right)
            not_correct = dfs(flip.right, target.left) and dfs(flip.left, target.right)

            return correct or not_correct

            
        return dfs(root1, root2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []
        self.totalPaths = 0
          
    def preorder(self, root, targetSum):
        if root is None:
            return 
        
        self.paths.append(root.val)
        
        self.preorder(root.left, targetSum)
        self.preorder(root.right, targetSum)
        s = 0
        
        for i in range(len(self.paths) - 1, -1, -1):
            s += self.paths[i]
            if s == targetSum:
                self.totalPaths += 1
                
        self.paths.pop(-1)
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.preorder(root, targetSum)
        return self.totalPaths
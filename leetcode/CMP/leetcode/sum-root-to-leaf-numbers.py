# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.calculateSum(root, 0)
    
    def calculateSum(self, node, currentSum):
        if node is None:
            return 0
        
        currentSum = currentSum * 10 + node.val
        
        if node.left is None and node.right is None:
            return currentSum
        
        leftSum = self.calculateSum(node.left, currentSum)
        rightSum = self.calculateSum(node.right, currentSum)
        
        return leftSum + rightSum
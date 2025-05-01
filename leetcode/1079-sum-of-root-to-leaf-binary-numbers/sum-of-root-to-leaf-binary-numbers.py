# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                path_value = int("".join(path), 2)
                path.pop()
                return path_value
            
            left_sum = dfs(node.left, path)
            right_sum = dfs(node.right, path)
            
            path.pop()
            
            return left_sum + right_sum
        
        return dfs(root, [])

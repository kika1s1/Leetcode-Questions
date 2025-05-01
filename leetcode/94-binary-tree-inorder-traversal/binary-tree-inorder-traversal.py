# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive way of inorder
        results = []
        # def dfs(root):
        #     if not root:
        #         return
        #     if root.left:
        #         dfs(root.left)
        #     result.append(root.val)
        #     if root.right:
        #         dfs(root.right)
        #     return result
        # return dfs(root)
        # iterative way
        output, stack = [], []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            
            else:
                
                node = stack.pop()
                output.append(node.val)
                root = node.right
                
        return output
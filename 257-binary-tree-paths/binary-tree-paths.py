# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node, path):
            if node: 
                path += str(node.val)
                if node.left or node.right:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)
                else:
                    result.append(path)
                    return 
        dfs(root, "")
        return result

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
                new_path = path + str(node.val)
                if node.left or node.right:
                    new_path += "->"
                    dfs(node.left, new_path)
                    dfs(node.right, new_path)
                else:
                    result.append(new_path)
        dfs(root, "")
        return result

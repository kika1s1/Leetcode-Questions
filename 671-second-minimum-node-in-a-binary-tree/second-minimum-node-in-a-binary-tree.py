# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result = set()
        def dfs(root):
            if root:
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
                result.add(root.val)
        dfs(root)
        if len(result) < 2:
            return -1
        result.discard(min(result))
        return min(result)
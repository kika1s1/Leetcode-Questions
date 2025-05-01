# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cnt = 0
        def dfs(current):
            nonlocal cnt
            if not current:
                return 0
            cnt +=1
            if current.left:
                dfs(current.left)
            if current.right:
                dfs(current.right)
            return cnt
        return dfs(root)
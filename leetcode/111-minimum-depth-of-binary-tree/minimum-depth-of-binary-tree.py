# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        minim = float("inf")
        def dfs(root, cnt):
            if not root:
                return float("inf")
            if not root.left and not root.right:
                return cnt
            left = dfs(root.left, cnt+1)
            right = dfs(root.right, cnt +1)
            return min(left, right)
        return dfs(root, 1)


        
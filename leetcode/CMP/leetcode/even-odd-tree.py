# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, 0)])
        d = {}
        while q:
            node, level = q.popleft()
            odd = level % 2
            if level not in d:
                d[level] = float('inf') if odd else 0
            if odd and (d[level] <= node.val or node.val % 2 != 0):
                return False
            if not odd and (d[level] >= node.val or node.val % 2 == 0):
                return False
            d[level] = node.val
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])
        return True
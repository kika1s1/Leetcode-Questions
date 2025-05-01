# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            sub = []
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                sub.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sub:
                result = []
                result.append(sub)
        return result[0][0]

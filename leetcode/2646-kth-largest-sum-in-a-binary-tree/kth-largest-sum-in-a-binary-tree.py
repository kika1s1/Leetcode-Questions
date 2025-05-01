# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        queue = deque([root])
        while queue:
            level = []
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level:
                result.append(sum(level))
        result.sort(reverse=True)
        return result[k-1] if k <= len(result)  else -1